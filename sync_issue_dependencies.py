#!/usr/bin/env python3
"""
Script to sync issue dependencies from ZenHub to GitHub.

Reads blocking/blocked-by relationships from ZenHub and creates corresponding
GitHub issue dependencies using the GitHub REST API.
"""

import os
import sys
import requests
import argparse
from typing import Dict, Optional, List
from dotenv import load_dotenv

from helpers import zenhub


class GitHubClient:
    """Client for interacting with GitHub REST API."""

    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get_repository_info(self, repo_id: int) -> Optional[Dict[str, str]]:
        """Get repository owner and name from GitHub ID."""
        try:
            response = requests.get(
                f"{self.base_url}/repositories/{repo_id}",
                headers=self.headers
            )
            response.raise_for_status()
            repo_data = response.json()
            return {
                "owner": repo_data["owner"]["login"],
                "name": repo_data["name"]
            }
        except requests.exceptions.RequestException as e:
            print(f"Error getting repository info for ID {repo_id}: {e}")
            return None

    def get_existing_dependencies(self, owner: str, repo: str, issue_number: int) -> List[int]:
        """Get list of issue IDs that are currently blocking the given issue."""
        try:
            response = requests.get(
                f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by",
                headers=self.headers
            )
            response.raise_for_status()
            dependencies = response.json()
            return [dep["id"] for dep in dependencies]
        except requests.exceptions.RequestException as e:
            print(f"Error getting existing dependencies for {owner}/{repo}#{issue_number}: {e}")
            return []

    def create_dependency(self, owner: str, repo: str, blocked_issue_number: int, blocking_issue_id: int) -> bool:
        """
        Create a dependency relationship where blocking_issue_id blocks blocked_issue_number.

        Args:
            owner: Repository owner
            repo: Repository name
            blocked_issue_number: Issue number that is being blocked
            blocking_issue_id: GitHub issue ID that is doing the blocking

        Returns:
            True if successful, False otherwise
        """
        payload = {"issue_id": blocking_issue_id}

        try:
            response = requests.post(
                f"{self.base_url}/repos/{owner}/{repo}/issues/{blocked_issue_number}/dependencies/blocked_by",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error creating dependency for {owner}/{repo}#{blocked_issue_number} blocked by issue ID {blocking_issue_id}: {e}")
            return False

    def get_issue_id(self, owner: str, repo: str, issue_number: int) -> Optional[int]:
        """Get the GitHub issue ID from owner/repo/issue_number."""
        try:
            response = requests.get(
                f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}",
                headers=self.headers
            )
            response.raise_for_status()
            issue_data = response.json()
            return issue_data["id"]
        except requests.exceptions.RequestException as e:
            print(f"Error getting issue ID for {owner}/{repo}#{issue_number}: {e}")
            return None


def main():
    """Main script execution."""
    # Load environment variables from .env file
    load_dotenv()

    workspace_choices = list(zenhub.WORKSPACE_NAMES.keys())
    parser = argparse.ArgumentParser(description="Sync issue dependencies from ZenHub to GitHub")
    parser.add_argument(
        "--workspace",
        required=True,
        choices=workspace_choices,
        help=f"Workspace name: {', '.join(workspace_choices)}"
    )
    parser.add_argument("--dry-run", action="store_true",
                       help="Print what would be done without making changes")

    args = parser.parse_args()

    # Get tokens from environment variables
    zenhub_token = os.getenv("ZENHUB_TOKEN")
    github_token = os.getenv("GITHUB_TOKEN")

    if not zenhub_token:
        print("Error: ZENHUB_TOKEN not found in environment variables or .env file")
        sys.exit(1)

    if not github_token:
        print("Error: GITHUB_TOKEN not found in environment variables or .env file")
        sys.exit(1)

    # Resolve workspace name to ID and get repos
    workspace_id = zenhub.WORKSPACE_NAMES[args.workspace]
    repos = zenhub.WORKSPACE_SETS[workspace_id]

    # Initialize clients
    endpoint = zenhub.api(zenhub_token)
    github = GitHubClient(github_token)

    # Get dependencies from ZenHub using the existing get_dependency_graph function
    print(f"Fetching dependencies from ZenHub workspace '{args.workspace}'...")
    dep_graph = zenhub.get_dependency_graph(endpoint, workspace_id, repos)

    # Extract edges from the NetworkX graph
    # Each edge is ((blocking_repo, blocking_issue_num), (blocked_repo, blocked_issue_num))
    dependencies = list(dep_graph.edges())
    print(f"Found {len(dependencies)} dependencies")

    # Cache for repository info to avoid repeated API calls
    repo_cache: Dict[int, Optional[Dict[str, str]]] = {}

    # Process each dependency
    created_count = 0
    skipped_count = 0

    for (blocking_repo, blocking_issue_num), (blocked_repo, blocked_issue_num) in dependencies:
        blocking_repo_id = blocking_repo.gh_id
        blocked_repo_id = blocked_repo.gh_id

        # Get repository info for both repos
        if blocked_repo_id not in repo_cache:
            repo_cache[blocked_repo_id] = github.get_repository_info(blocked_repo_id)
        if blocking_repo_id not in repo_cache:
            repo_cache[blocking_repo_id] = github.get_repository_info(blocking_repo_id)

        blocked_repo_info = repo_cache[blocked_repo_id]
        blocking_repo_info = repo_cache[blocking_repo_id]

        if not blocked_repo_info or not blocking_repo_info:
            print(f"Skipping dependency due to missing repository info")
            skipped_count += 1
            continue

        # Get the GitHub issue ID for the blocking issue
        blocking_issue_id = github.get_issue_id(
            blocking_repo_info["owner"],
            blocking_repo_info["name"],
            blocking_issue_num
        )

        if not blocking_issue_id:
            print(f"Skipping: Could not get issue ID for {blocking_repo_info['owner']}/{blocking_repo_info['name']}#{blocking_issue_num}")
            skipped_count += 1
            continue

        # Check if dependency already exists
        existing_deps = github.get_existing_dependencies(
            blocked_repo_info["owner"],
            blocked_repo_info["name"],
            blocked_issue_num
        )

        if blocking_issue_id in existing_deps:
            print(f"Dependency already exists: {blocking_repo_info['owner']}/{blocking_repo_info['name']}#{blocking_issue_num} blocks {blocked_repo_info['owner']}/{blocked_repo_info['name']}#{blocked_issue_num}")
            skipped_count += 1
            continue

        # Create the dependency
        dependency_desc = f"{blocking_repo_info['owner']}/{blocking_repo_info['name']}#{blocking_issue_num} blocks {blocked_repo_info['owner']}/{blocked_repo_info['name']}#{blocked_issue_num}"

        if args.dry_run:
            print(f"[DRY RUN] Would create dependency: {dependency_desc}")
            continue

        print(f"Creating dependency: {dependency_desc}")
        if github.create_dependency(
            blocked_repo_info["owner"],
            blocked_repo_info["name"],
            blocked_issue_num,
            blocking_issue_id
        ):
            created_count += 1
        else:
            skipped_count += 1

    print(f"\nSummary:")
    print(f"  Created: {created_count} dependencies")
    print(f"  Skipped: {skipped_count} dependencies")
    if args.dry_run:
        print("  (This was a dry run - no changes were made)")


if __name__ == "__main__":
    main()
