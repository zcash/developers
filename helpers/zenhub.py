import networkx as nx
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from helpers.repos import ALL_REPOS, CORE_REPOS, TFL_REPOS, WALLET_REPOS, ZF_REPOS, ZF_FROST_REPOS, Repo
from zenhub_schema import zenhub_schema

WORKSPACE_SETS = {
    # ecc-core
    '5dc1fd615862290001229f21': CORE_REPOS + TFL_REPOS,
    # ecc-wallet
    '5db8aa0244512d0001e0968e': WALLET_REPOS,
    # zf
    '5fb24d9264a3e8000e666a9e': ZF_REPOS,
    # zf-frost
    '607d75e0169bd50011d5410f': ZF_FROST_REPOS,
}

REPO_MAP = {repo.gh_id: repo for repo in ALL_REPOS}


def repo_lookup(repo_id):
    try:
        return REPO_MAP[repo_id]
    except KeyError:
        return Repo(None, repo_id, None)


def api(token):
    return HTTPEndpoint(
        'https://api.zenhub.com/public/graphql',
        {'Authorization': 'Bearer %s' % token},
    )


def fetch_workspace_repos(op, workspace_id):
    repos = op.workspace(id=workspace_id).repositories()
    repos.id()
    repos.gh_id()
    repos.name()
    repos.owner.login()


def get_workspace_repos(endpoint, workspaces):
    repos = []

    for workspace_id in workspaces:
        op = Operation(zenhub_schema.Query)
        fetch_workspace_repos(op, workspace_id)

        d = endpoint(op)
        data = op + d

        if hasattr(data.workspace, 'repositories'):
            repos += [
                ((repo.owner.login, repo.name), repo.gh_id, repo.id)
                for repo in data.workspace.repositories
            ]

    return repos


def fetch_workspace_graph(op, workspace_id, repos, cursor):
    dependencies = op.workspace(id=workspace_id).issue_dependencies(
        # TODO: This causes a 500 Internal Server Error. We need the ZenHub repo IDs here,
        # not the GitHub repo IDs (which the previous REST API used).
        # repository_ids=repos,
        first=100,
        after=cursor,
    )
    dependencies.nodes.id()
    dependencies.nodes.blocked_issue.number()
    dependencies.nodes.blocked_issue.repository.gh_id()
    dependencies.nodes.blocking_issue.number()
    dependencies.nodes.blocking_issue.repository.gh_id()
    dependencies.page_info.has_next_page()
    dependencies.page_info.end_cursor()


# Fetches the dependency graph involving the given `repos` from the given `workspace_id`.
#
# `repos` is a list of `Repo` objects.
#
# Returns a list of `(blocking, blocked)` tuples corresponding to DAG edges.
# `blocking` and `blocked` are both `(Repo, issue_number)` tuples.
def get_dependency_graph(endpoint, workspace_id, repos):
    edges = []
    cursor = None

    while True:
        op = Operation(zenhub_schema.Query)
        fetch_workspace_graph(op, workspace_id, repos, cursor)

        d = endpoint(op)
        data = op + d

        if hasattr(data.workspace, 'issue_dependencies'):
            dependencies = data.workspace.issue_dependencies
            edges += [
                (
                    (repo_lookup(node.blocking_issue.repository.gh_id), node.blocking_issue.number),
                    (repo_lookup(node.blocked_issue.repository.gh_id), node.blocked_issue.number),
                )
                for node in dependencies.nodes
            ]

            if dependencies.page_info.has_next_page:
                cursor = dependencies.page_info.end_cursor
                print('.', end='', flush=True)
            else:
                print()
                break
        else:
            print()
            break

    return nx.DiGraph(edges)


def fetch_epics(op, workspace_id, repos, cursor):
    epics = op.workspace(id=workspace_id).epics(
        # TODO: This causes a 500 Internal Server Error. We need the ZenHub repo IDs here,
        # not the GitHub repo IDs (which the previous REST API used).
        # repository_ids=repos,
        first=100,
        after=cursor,
    )
    epics.nodes.id()
    epics.nodes.issue.number()
    epics.nodes.issue.repository.gh_id()
    epics.page_info.has_next_page()
    epics.page_info.end_cursor()


def get_epics(endpoint, workspace_id, repos):
    epics = []
    cursor = None

    while True:
        op = Operation(zenhub_schema.Query)
        fetch_epics(op, workspace_id, repos, cursor)

        d = endpoint(op)
        data = op + d

        if hasattr(data.workspace, 'epics'):
            epics_page = data.workspace.epics
            epics += [
                (node.id, (repo_lookup(node.issue.repository.gh_id), node.issue.number))
                for node in epics_page.nodes
            ]

            if epics_page.page_info.has_next_page:
                cursor = epics_page.page_info.end_cursor
                print('.', end='', flush=True)
            else:
                print()
                break
        else:
            print()
            break

    return epics


def fetch_epic_issues(op, workspace_id, epic_id, cursor):
    epic = op.workspace(id=workspace_id).epics(ids=[epic_id])
    child_issues = epic.nodes.child_issues(
        first=100,
        after=cursor,
    )
    child_issues.nodes.number()
    child_issues.nodes.repository.gh_id()
    child_issues.page_info.has_next_page()
    child_issues.page_info.end_cursor()


def get_epic_issues(endpoint, workspace_id, epic_id):
    epic_issues = []
    cursor = None

    while True:
        op = Operation(zenhub_schema.Query)
        fetch_epic_issues(op, workspace_id, epic_id, cursor)

        d = endpoint(op)
        data = op + d

        epic = data.workspace.epics.nodes[0]
        epic_issues += [
            (repo_lookup(node.repository.gh_id), node.number)
            for node in epic.child_issues.nodes
        ]

        if epic.child_issues.page_info.has_next_page:
            cursor = epic.child_issues.page_info.end_cursor
            print('.', end='', flush=True)
        else:
            print()
            break

    return epic_issues
