#!/usr/bin/env python3

# ZenHub issue dependency graph generator for the ECC core team.
# Author: jack@electriccoin.co
# Last updated: 2021-05-07

import drest
import networkx as nx

import mimetypes
import os
from textwrap import wrap
from urllib.parse import urlparse

from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from github_schema import github_schema as schema

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
ZENHUB_TOKEN = os.environ.get('ZENHUB_TOKEN')

REPOS = {
    26987049: ('zcash', 'zcash'),
    47279130: ('zcash', 'zips'),
    85334928: ('zcash', 'librustzcash'),
    133857578: ('zcash-hackworks', 'zcash-test-vectors'),
    290019239: ('zcash', 'halo2'),
    305835578: ('zcash', 'orchard'),
}

# Whether to include subgraphs where all issues and PRs are closed.
INCLUDE_FINISHED = False

# Whether to group issues and PRs by milestone.
SHOW_MILESTONES = False


class GitHubIssue:
    def __init__(self, repo_id, issue_number, data):
        self.repo_id = repo_id
        self.issue_number = issue_number
        self.milestone = None

        if data is not None:
            self.title = data['title']
            self.is_pr = 'merged' in data
            self.url = data['url']
            self.state = 'closed' if data['state'] in ['CLOSED', 'MERGED'] else 'open'
            if 'milestone' in data and data['milestone']:
                self.milestone = data['milestone']['title']
        else:
            # If we can't fetch issue data, assume we don't care.
            self.title = ''
            self.url = None
            self.is_pr = False
            self.state = 'closed'

    def __repr__(self):
        if self.repo_id in REPOS:
            repo = '/'.join(REPOS[self.repo_id])
        else:
            repo = self.repo_id
        return '%s#%d' % (repo, self.issue_number)

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

    # Fetch the issues within the graph.
    mapping = download_issues(gapi, dg.nodes)

    # Relable the graph
    dg = nx.relabel_nodes(dg, mapping)

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

    # TODO:
    # - Automatically prune edges between closed nodes, not just fully-closed subgraphs.

    do_next = [n for (n, degree) in dg.in_degree(weight='is_open') if degree == 0 and n.state != 'closed']

    # Apply style annotations.
    for n in dg:
        attrs = dg.nodes[n]
        if n.title:
            attrs['label'] = '\n'.join(['%s' % n] + wrap(n.title, 25))
        attrs['fillcolor'] = '#fad8c7' if n.state == 'closed' else '#c2e0c6'
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

    # Draw the result!
    ag.graph_attr['rankdir'] = 'LR'
    ag.layout(prog='dot')
    os.makedirs('public', exist_ok=True)
    ag.draw('public/zcash-core-dag.svg')


if __name__ == '__main__':
    if GITHUB_TOKEN and ZENHUB_TOKEN:
        main()
    else:
        print('Please set the GITHUB_TOKEN and ZENHUB_TOKEN environment variables.')
