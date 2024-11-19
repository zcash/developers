#!/usr/bin/env python3

import networkx as nx
from str2bool import str2bool as strtobool

import itertools
import os
import re
from textwrap import wrap
from urllib.parse import urlparse

from helpers import github, repos as repositories, zenhub

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
ZENHUB_TOKEN = os.environ.get('ZENHUB_TOKEN')

# IDs of repos we look for releases in.
RUST = 85334928
ANDROID_SDK = 151763639
SWIFT_SDK = 185480114
ZASHI_ANDROID = 390808594
ZASHI_IOS = 387551125

REPOS = github.CORE_REPOS + github.WALLET_REPOS

RELEASE_MATRIX = {
    RUST: [ANDROID_SDK, SWIFT_SDK],
    ANDROID_SDK: [ZASHI_ANDROID],
    SWIFT_SDK: [ZASHI_IOS],
    ZASHI_ANDROID: [],
    ZASHI_IOS: []
}


class Release:
    def __init__(self, repo_id, child):
        self.repo_id = repo_id

        # Extract version number from title
        if repo_id == RUST:
            self.version = re.search(r'zcash_[^ ]+ \d+(\.\d+)+', child.title).group()
            self.version_ints = tuple(int(x) for x in self.version.split(' ')[1].split('.'))
        else:
            self.version = re.search(r'\d+(\.\d+)+', child.title).group()
            self.version_ints = tuple(int(x) for x in self.version.split('.'))

        self.is_closed = child.state == 'closed'
        self.url = child.url

    def __repr__(self):
        return self.version

    def __eq__(self, other):
        return (self.repo_id, self.version) == (other.repo_id, other.version)

    def __hash__(self):
        return hash((self.repo_id, self.version))

    def __lt__(self, other):
        return self.version_ints < other.version_ints


def build_release(row, repo_id):
    child = row.get(repo_id)
    if child is None:
        return None
    else:
        return Release(repo_id, child)


class ReleasePipeline:
    def __init__(self, row):
        self.rust = build_release(row, RUST)
        self.android_sdk = build_release(row, ANDROID_SDK)
        self.swift_sdk = build_release(row, SWIFT_SDK)
        self.zashi_android = build_release(row, ZASHI_ANDROID)
        self.zashi_ios = build_release(row, ZASHI_IOS)

    def __repr__(self):
        return '%s | %s | %s | %s | %s' % self.columns()

    def __eq__(self, other):
        return self.columns() == other.columns()

    def __hash__(self):
        return hash(self.columns())

    def __lt__(self, other):
        return self.columns() < other.columns()

    def columns(self):
        return (
            self.rust,
            self.android_sdk,
            self.swift_sdk,
            self.zashi_android,
            self.zashi_ios,
        )

def build_release_matrix_from(dg, issue, repo_id):
    acc = []
    for child in dg.neighbors(issue):
        if child.repo.gh_id == repo_id and 'C-release' in child.labels:
            # Fetch the rows that each child's downstreams need rendered.
            child_deps = [
                build_release_matrix_from(dg, child, dep_repo)
                for dep_repo in RELEASE_MATRIX.get(repo_id)
            ]

            # Merge the rows from each downstream repo together.
            child_releases = [
                {k: v for d in prod for k, v in d.items()}
                for prod in itertools.product(*child_deps)
            ]

            if len(child_releases) > 0:
                for rec in child_releases:
                    rec[repo_id] = child
            else:
                child_releases = [{repo_id: child}]

            acc.extend(child_releases)
        else:
            acc.extend(build_release_matrix_from(dg, child, repo_id))

    return acc

def main():
    gapi = github.api(GITHUB_TOKEN)
    zapi = zenhub.api(ZENHUB_TOKEN)

    print('Fetching tracked issues')
    tracked_issues = github.download_issues_with_labels(gapi, ['C-tracked-bug', 'C-tracked-feature'], REPOS)

    # The repos we care about are now:
    # - Any repo containing a tracked issue.
    # - The wallet repos where releases occur.
    repos = set([repo for (repo, _) in tracked_issues] + [
        repositories.LIBRUSTZCASH,
        repositories.ZCASH_ANDROID_WALLET_SDK,
        repositories.ZCASH_LIGHT_CLIENT_FFI,
        repositories.ZCASH_SWIFT_WALLET_SDK,
        repositories.ZASHI_ANDROID,
        repositories.ZASHI_IOS,
    ])
    workspaces = {
        workspace_id: [repo for repo in repos if repo in repos]
        for (workspace_id, _) in zenhub.WORKSPACE_SETS.items()
    }

    # Build the full dependency graph from ZenHub's per-workspace API.
    print('Fetching graph')
    dg = nx.compose_all([
        zenhub.get_dependency_graph(zapi, workspace_id, repos)
        for (workspace_id, repos) in workspaces.items()
        if len(repos) > 0
    ])

    print('Rendering deployment pipeline')

    # Ensure that the tracked issues all exist in the graph. This is a no-op for
    # issues that are already present.
    start_at = set([issue for issue in tracked_issues])
    for i in start_at:
        dg.add_node(i)

    # Replace the graph with the subgraph that only includes the tracked
    # issues and their descendants.
    descendants = [nx.descendants(dg, n) for n in start_at]
    dg = nx.subgraph(dg, start_at.union(*descendants))

    # Fetch the issues within the graph.
    mapping = github.download_issues(gapi, dg.nodes, repos)

    # Relabel the graph
    dg = nx.relabel_nodes(dg, mapping)

    # Filter out unknown issues
    unknown = [n for n in dg if n.repo not in repos]
    if len(unknown) > 0:
        dg.remove_nodes_from(unknown)

    # Apply property annotations
    for (source, sink) in dg.edges:
        attrs = dg.edges[source, sink]
        attrs['is_open'] = 0 if source.state == 'closed' else 1

    # Render the HTML version!
    html_header = '''<!DOCTYPE html>
<html>
  <head>
    <title>Zashi Pipeline</title>

    <style>
      body {
        color: #1f2328;
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
        font-size: 14px;
        line-height: 1.5;
        word-wrap: break-word;
      }
      a {
        color: #0969da;
      }
      table {
        border-collapse: collapse;
        width: 100%;
        width: max-content;
        max-width: 100%;
        overflow: auto;
      }
      table tr {
        border-top: 1px solid #d1d9e0b3;
      }
      table th, table td {
        border: 1px solid #d1d9e0b3;
        padding: 6px 13px;
        text-align: center;
      }

      @media (prefers-color-scheme: dark) {
        body {
          background-color: #121212;
          color: #f0f6fc;
        }
        a {
          color: #4493f8;
        }
        table tr {
            border-top: 1px solid #3d444db3;
        }
        table th, table td {
            border: 1px solid #3d444db3;
        }
      }
    </style>
  </head>
  <body>
    <h1>Zashi Pipeline</h1>
    <p>🐞 = bug, 💡 = feature, ✅ = implemented / released, 🛑 = unfinished, 📥 = unassigned / DAG needs updating</p>
    <table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Issue</th>
          <th>Rust crate</th>
          <th>Android SDK</th>
          <th>Swift SDK</th>
          <th>Zashi Android</th>
          <th>Zashi iOS</th>
        </tr>
      </thead>
      <tbody>
'''
    html_footer = '''
      </tbody>
    </table>
  </body>
</html>
'''
    with open('public/zashi-pipeline.html', 'w') as f:
        f.write(html_header)

        for issue in tracked_issues.values():
            rows = [ReleasePipeline(row) for row in build_release_matrix_from(dg, issue, RUST)]

            # If we traversed the entire graph and there are no releases downstream of the
            # issue, show this as an empty row.
            if len(rows) == 0:
                rows = [ReleasePipeline({})]

            # Deduplicate rows
            rows = list(dict.fromkeys(rows))

            # At this point we have a row for each path through the DAG from a tracked bug
            # or feature through a unique set of releases. However, as individual releases
            # within a repo have graph edges between them (e.g. Zashi Android 1.2.3 blocks
            # on Zashi Android 1.2.2), this produces additional rows that we don't care
            # about:
            #
            # - The Zashi repos don't follow SemVer, and are also the ends of the paths;
            #   all we care about here is the earliest Zashi Android and Zashi iOS release
            #   that includes the bug or feature.
            # - The Android and Swift SDKs don't appear to follow SemVer (even though e.g.
            #   Swift Package Manager assumes it), so we also don't care about tracking
            #   whether a bug or feature makes it into both a point release and the next
            #   non-point release.
            # - The Rust crates do follow SemVer; if a bug or feature is deployed in a
            #   point release as a backwards-compatible change, we want to ensure that it
            #   also gets merged back into `main` so that we don't accidentally omit it
            #   from the next breaking crate release. However, we don't need to track
            #   subsequent breaking crate releases after that, because we develop breaking
            #   releases in `main`.

            # Create a map from Rust releases to lists of rows involving that release.
            rust_map = {}
            for row in rows:
                if row.rust in rust_map:
                    rust_map[row.rust].append(row)
                else:
                    rust_map[row.rust] = [row]

            # Remove the Rust releases that we don't need to track.
            rust_releases = list(rust_map.keys())
            rust_releases.sort(reverse=True)
            next_rust_release = rust_releases.pop()
            while len(rust_releases) > 0:
                rust_release = rust_releases.pop()
                if next_rust_release.version_ints[:-1] == rust_release.version_ints[:-1]:
                    # This is a subsequent point release; ignore.
                    del rust_map[rust_release]
                else:
                    # This is the subsequent non-point release.
                    if next_rust_release.version_ints[-1] == 0:
                        # The next release is also a non-point release; ignore this one.
                        del rust_map[rust_release]

                    # Ignore all subsequent releases.
                    for rust_release in rust_releases:
                        del rust_map[rust_release]
                    break

            # For the tracked Rust releases, select the row that has the earliest version
            # number across each of the SDKs and Zashi apps.
            rows = []
            for rust_release in rust_map.values():
                rust_release.sort()
                rows.append(rust_release[0])

            for i, row in enumerate(rows):
                f.write('<tr>')

                if i == 0:
                    rowspan = ''
                    if len(rows) > 1:
                        rowspan = ' rowspan="{}"'.format(len(rows))

                    f.write('<td{}>{}</td>'.format(
                        rowspan,
                        '🐞' if 'C-tracked-bug' in issue.labels else '💡',
                    ))
                    f.write('<td{}>{} <a href="{}">{}</a></td>'.format(
                        rowspan,
                        '✅' if issue.state == 'closed' else '🛑',
                        issue.url,
                        issue.title,
                    ))

                for release in row.columns():
                    if release is None:
                        # Release not found in this repo
                        f.write('<td>📥</td>')
                    else:
                        f.write('<td>{} <a href="{}">{}</a></td>'.format(
                            '✅' if release.is_closed else '🛑',
                            release.url,
                            release.version,
                        ))
                f.write('</tr>')

        f.write(html_footer)


if __name__ == '__main__':
    if GITHUB_TOKEN and ZENHUB_TOKEN:
        main()
    else:
        print('Please set the GITHUB_TOKEN and ZENHUB_TOKEN environment variables.')
