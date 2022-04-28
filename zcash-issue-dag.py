#!/usr/bin/env python3

# ZenHub issue dependency graph generator for the ECC core team.
# Author: jack@electriccoin.co
# Last updated: 2021-05-07

import drest
import networkx as nx

from distutils.util import strtobool
import mimetypes
import os
from textwrap import wrap
from urllib.parse import urlparse

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from github_schema import github_schema as schema

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
ZENHUB_TOKEN = os.environ.get('ZENHUB_TOKEN')

DAG_VIEW = os.environ.get('DAG_VIEW', 'core')

CORE_REPOS = {
    26987049: ('zcash', 'zcash'),
    47279130: ('zcash', 'zips'),
    48303644: ('zcash', 'incrementalmerkletree'),
    85334928: ('zcash', 'librustzcash'),
    133857578: ('zcash-hackworks', 'zcash-test-vectors'),
    290019239: ('zcash', 'halo2'),
    305835578: ('zcash', 'orchard'),
    344239327: ('zcash', 'pasta_curves'),
}

HALO2_REPOS = {
    290019239: ('zcash', 'halo2'),
    344239327: ('zcash', 'pasta_curves'),
}

WALLET_REPOS = {
    85334928: ('zcash', 'librustzcash'),
    151763639: ('zcash', 'zcash-android-wallet-sdk'),
    159714694: ('zcash', 'lightwalletd'),
    185480114: ('zcash', 'ZcashLightClientKit'),
    387551125: ('zcash', 'secant-ios-wallet'),
    390808594: ('zcash', 'secant-android-wallet'),
    270825987: ('zcash-hackworks', 'MnemonicSwift'),
    439137887: ('zcash-hackworks', 'zcash-light-client-ffi'),
}

ANDROID_REPOS = {
    390808594: ('zcash', 'secant-android-wallet'),
    151763639: ('zcash', 'zcash-android-wallet-sdk')
}

IOS_REPOS = {
    387551125: ('zcash', 'secant-ios-wallet'),
    185480114: ('zcash', 'ZcashLightClientKit'),
    270825987: ('zcash-hackworks', 'MnemonicSwift'),
    439137887: ('zcash-hackworks', 'zcash-light-client-ffi')
}

ZF_REPOS = {
    205255683: ('ZcashFoundation', 'zebra'),
    225479018: ('ZcashFoundation', 'redjubjub'),
    235651437: ('ZcashFoundation', 'ed25519-zebra'),
    279422254: ('ZcashFoundation', 'zcash_script'),
}

ZF_FROST_REPOS = {
    437862440: ('ZcashFoundation', 'frost'),
}

REPO_SETS = {
    'core': CORE_REPOS,
    'halo2': HALO2_REPOS,
    'wallet': WALLET_REPOS,
    'wallet-ios': IOS_REPOS,
    'wallet-android': ANDROID_REPOS,
    'zf': ZF_REPOS,
    'zf-frost': ZF_FROST_REPOS,
}

REPOS = REPO_SETS[DAG_VIEW]

# Whether to include subgraphs where all issues and PRs are closed.
INCLUDE_FINISHED = strtobool(os.environ.get('INCLUDE_FINISHED', 'false'))

# Whether to remove closed issues and PRs that are not downstream of open ones.
PRUNE_FINISHED = strtobool(os.environ.get('PRUNE_FINISHED', 'true'))

# Whether to group issues and PRs by milestone.
SHOW_MILESTONES = strtobool(os.environ.get('SHOW_MILESTONES', 'false'))

# Whether to group issues and PRs by ZenHub epics.
SHOW_EPICS = strtobool(os.environ.get('SHOW_EPICS', 'false'))


class GitHubIssue:
    def __init__(self, repo_id, issue_number, data):
        self.repo_id = repo_id
        self.issue_number = issue_number
        self.milestone = None

        if data is not None:
            labels = [label['name'] for label in data['labels']['nodes']]
            self.title = data['title']
            self.is_pr = 'merged' in data
            self.is_committed = 'S-committed' in labels
            self.url = data['url']
            self.state = 'closed' if data['state'] in ['CLOSED', 'MERGED'] else 'open'
            if 'milestone' in data and data['milestone']:
                self.milestone = data['milestone']['title']
        else:
            # If we can't fetch issue data, assume we don't care.
            self.title = ''
            self.url = None
            self.is_pr = False
            self.is_committed = False
            self.state = 'closed'

    def __repr__(self):
        if self.repo_id in REPOS:
            repo = '/'.join(REPOS[self.repo_id])
            return '%s#%d' % (repo, self.issue_number)
        else:
            return 'Unknown'

    def __eq__(self, other):
        return (self.repo_id, self.issue_number) == (other.repo_id, other.issue_number)

    def __hash__(self):
        return hash((self.repo_id, self.issue_number))

def fetch_issues(op, issues):
    repos = set([repo for (repo, _) in issues])
    repos = {repo: [issue for (r, issue) in issues if r == repo] for repo in repos}

    for (repo, issues) in repos.items():
        conn = op.repository(
            owner=REPOS[repo][0],
            name=REPOS[repo][1],
            __alias__='repo%d' % repo,
        )

        for issue in issues:
            res = conn.issue_or_pull_request(number=issue, __alias__='issue%d' % issue)
            for typ in [schema.Issue, schema.PullRequest]:
                node = res.__as__(typ)
                node.labels(first=50).nodes().name()
                node.state()
                node.milestone().title()
                node.title()
                node.url()
                if typ == schema.PullRequest:
                    node.merged()

def download_issues(endpoint, nodes):
    issues = [(repo, issue) for (repo, issue) in nodes if repo in REPOS]

    ret = {}
    for (repo, issue) in [(repo, issue) for (repo, issue) in nodes if repo not in REPOS]:
        ret[(repo, issue)] = GitHubIssue(repo, issue, None)

    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    for issues in chunks(issues, 50):
        op = Operation(schema.Query)
        fetch_issues(op, issues)

        d = endpoint(op)
        data = (op + d)

        for (repo, issue) in issues:
            ret[(repo, issue)] = GitHubIssue(repo, issue, data['repo%d' % repo]['issue%d' % issue])

    return ret


class ZHDepsResourceHandler(drest.resource.ResourceHandler):
    def get(self, repo_id):
        path = '/repositories/%d/dependencies' % repo_id

        try:
            response = self.api.make_request('GET', path, {})
        except drest.exc.dRestRequestError as e:
            msg = "%s (repo_id: %s)" % (e.msg, repo_id)
            raise drest.exc.dRestRequestError(msg, e.response)

        def issue(json):
            return (int(json['repo_id']), int(json['issue_number']))

        return nx.DiGraph([
            (issue(edge['blocking']), issue(edge['blocked']))
            for edge in response.data['dependencies']
        ])

class ZHEpicsResourceHandler(drest.resource.ResourceHandler):
    def get(self, repo_id):
        path = '/repositories/%d/epics' % repo_id

        try:
            response = self.api.make_request('GET', path, {})
        except drest.exc.dRestRequestError as e:
            msg = "%s (repo_id: %s)" % (e.msg, repo_id)
            raise drest.exc.dRestRequestError(msg, e.response)

        return [i['issue_number'] for i in response.data['epic_issues']]

class ZHEpicsIssuesResourceHandler(drest.resource.ResourceHandler):
    def get(self, repo_id, epic_id):
        path = '/repositories/%d/epics/%d' % (repo_id, epic_id)

        try:
            response = self.api.make_request('GET', path, {})
        except drest.exc.dRestRequestError as e:
            msg = "%s (repo_id: %s)" % (e.msg, repo_id)
            raise drest.exc.dRestRequestError(msg, e.response)

        return [(i['repo_id'], i['issue_number']) for i in response.data['issues']]

class ZenHubAPI(drest.api.API):
    class Meta:
        baseurl = 'https://api.zenhub.com/p1'
        extra_headers = {
            'X-Authentication-Token': ZENHUB_TOKEN,
            'Content-Type': 'application/json',
        }

    def __init__(self, *args, **kw):
        super(ZenHubAPI, self).__init__(*args, **kw)
        self.add_resource('dependencies', ZHDepsResourceHandler)
        self.add_resource('epics', ZHEpicsResourceHandler)
        self.add_resource('epics_issues', ZHEpicsIssuesResourceHandler)

    def auth(self, *args, **kw):
        pass


def main():
    gapi = HTTPEndpoint(
        'https://api.github.com/graphql',
        {'Authorization': 'bearer %s' % GITHUB_TOKEN},
    )
    zapi = ZenHubAPI()

    # Build the full dependency graph from ZenHub's per-repo APIs.
    dg = nx.compose_all([zapi.dependencies.get(x) for x in REPOS])

    if SHOW_EPICS:
        epics_issues = []
        for repo_id in REPOS:
            for epic_id in zapi.epics.get(repo_id):
                epics_issues.append((repo_id, epic_id))

        epics_mapping = download_issues(gapi, epics_issues)
        epics_mapping = {k: v for (k, v) in epics_mapping.items() if v.state != 'closed'}
        issues_by_epic = {}
        for (i, ((repo_id, epic_id), epic)) in enumerate(epics_mapping.items()):
            issues = set(zapi.epics_issues.get(repo_id, epic_id))
            issues_by_epic[epic] = issues
            for i in issues:
                # zapi.dependencies only returns nodes that have some connection,
                # but we'd like to show all issues from epics even if they are
                # disconnected.
                dg.add_node(i)

    # Fetch the issues within the graph.
    mapping = download_issues(gapi, dg.nodes)

    # Relabel the graph
    dg = nx.relabel_nodes(dg, mapping)

    # Filter out unknown issues
    unknown = [n for n in dg if n.repo_id not in REPOS]
    if len(unknown) > 0:
        dg.remove_nodes_from(unknown)

    # Apply property annotations
    for (source, sink) in dg.edges:
        attrs = dg.edges[source, sink]
        attrs['is_open'] = 0 if source.state == 'closed' else 1

    if not INCLUDE_FINISHED:
        # Identify the disconnected subgraphs.
        subgraphs = [dg.subgraph(c) for c in nx.connected_components(dg.to_undirected())]

        # Identify subgraphs comprised entirely of closed issues.
        ignore = [g for g in subgraphs if all([n.state == 'closed' for n in g])]

        # Remove fully-closed subgraphs.
        if len(ignore) > 0:
            dg.remove_nodes_from(nx.compose_all(ignore))

    # Prune nodes that are not downstream of any open issues.
    if PRUNE_FINISHED:
        # - It would be nice to keep the most recently-closed issues on the DAG, but
        #   dg.out_degree seems to be broken...
        to_prune = [n for (n, degree) in dg.in_degree() if degree == 0 and n.state == 'closed']
        while len(to_prune) > 0:
            dg.remove_nodes_from(to_prune)
            to_prune = [n for (n, degree) in dg.in_degree() if degree == 0 and n.state == 'closed']

    do_next = [n for (n, degree) in dg.in_degree(weight='is_open') if degree == 0 and n.state != 'closed']

    # Apply style annotations.
    for n in dg:
        attrs = dg.nodes[n]
        if n.title:
            attrs['label'] = '\n'.join(['%s' % n] + wrap(n.title, 25))
        if n.state == 'closed':
            attrs['class'] = 'closed'
            attrs['fillcolor'] = '#fad8c7'
        elif n.is_committed:
            attrs['class'] = 'committed'
            attrs['fillcolor'] = '#a6cfff'
        else:
            attrs['class'] = 'open'
            attrs['fillcolor'] = '#c2e0c6'
        attrs['penwidth'] = 2 if n in do_next else 1
        attrs['shape'] = 'component' if n.is_pr else 'box'
        attrs['style'] = 'filled'
        if n.url:
            attrs['URL'] = n.url
            attrs['target'] = '_blank'

    ag = nx.nx_agraph.to_agraph(dg)

    if SHOW_MILESTONES:
        # Identify milestone nbunches
        milestones = {n.milestone: [] for n in dg}
        for m in milestones:
            milestones[m] = [n for n in dg if n.milestone == m]
        del milestones[None]
        for (i, (milestone, nodes)) in enumerate(milestones.items()):
            ag.add_subgraph(nodes, 'cluster_%d' % i, label=milestone, color='blue')

    if SHOW_EPICS:
        for (i, (epic, issues)) in enumerate(issues_by_epic.items()):
            issues = [n for n in dg if (n.repo_id, n.issue_number) in issues]
            if issues:
                ag.add_subgraph(issues, 'cluster_%d' % i, label=epic.title, color='blue')

    # Draw the result!
    ag.graph_attr['rankdir'] = 'LR'
    ag.graph_attr['stylesheet'] = 'zcash-dag.css'
    ag.layout(prog='dot')
    os.makedirs('public', exist_ok=True)
    ag.draw('public/zcash-%s-dag.svg' % DAG_VIEW)

    # Render the HTML version!
    with open('public/zcash-%s-dag.svg' % DAG_VIEW) as f:
        svg_data = f.read()
    svg_start = svg_data.find('<svg')
    html_data = '''<!DOCTYPE html>
<html>
  <head>
    <title>Zcash %s DAG</title>

    <!-- Pan/zoom SVGs -->
    <script src="https://bumbu.me/svg-pan-zoom/dist/svg-pan-zoom.min.js"></script>

    <link rel="stylesheet" href="zcash-dag.css">
    <style>
      @media (prefers-color-scheme: dark) {
        body {
          /* Material dark theme surface colour */
          background-color: #121212;
        }
      }
    </style>
  </head>
  <body>
    <div id="dag">%s</div>

    <script>
      svgPanZoom('#dag > svg', {
        zoomScaleSensitivity: 0.4
      });
    </script>
  </body>
</html>
''' % (DAG_VIEW, svg_data[svg_start:])
    with open('public/zcash-%s-dag.html' % DAG_VIEW, 'w') as f:
        f.write(html_data)


if __name__ == '__main__':
    if GITHUB_TOKEN and ZENHUB_TOKEN:
        main()
    else:
        print('Please set the GITHUB_TOKEN and ZENHUB_TOKEN environment variables.')
