#!/usr/bin/env python3

# ZenHub issue dependency graph generator for the ECC core team.
# Author: jack@electriccoin.co
# Last updated: 2021-05-07

import networkx as nx

from str2bool import str2bool as strtobool
import os
from textwrap import wrap
from urllib.parse import urlparse

from helpers import github, zenhub

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
ZENHUB_TOKEN = os.environ.get('ZENHUB_TOKEN')

DAG_VIEW = os.environ.get('DAG_VIEW', 'core')

REPOS = github.REPO_SETS[DAG_VIEW]

WORKSPACES = {
    workspace_id: [repo_id for repo_id in repos if repo_id in REPOS]
    for (workspace_id, repos) in zenhub.WORKSPACE_SETS.items()
}

SUPPORTED_CATEGORIES = set(['releases', 'targets'])
def cats(s):
    return set([x.strip() for x in s.split(',')]) - set([''])

# If set, removes all issues and PRs that are not ancestors of the given issues.
# This can be used to render a sub-graph focused on one area.
#
# Format is ORG/REPO#ISSUE[,ORG/REPO#ISSUE[, ..]]
TERMINATE_AT = cats(os.environ.get('TERMINATE_AT', ''))

# Whether to remove issues and PRs that are not target or release issues.
ONLY_INCLUDE = cats(os.environ.get('ONLY_INCLUDE', ''))

# Whether to include subgraphs where all issues and PRs are closed.
INCLUDE_FINISHED = strtobool(os.environ.get('INCLUDE_FINISHED', 'false'))

# Whether to remove closed issues and PRs that are not downstream of open ones.
# When set to 'targets' or 'releases', only issues upstream of a closed target
# or release issue will be removed.
PRUNE_FINISHED = os.environ.get('PRUNE_FINISHED', 'true')

# Whether to group issues and PRs by milestone.
SHOW_MILESTONES = strtobool(os.environ.get('SHOW_MILESTONES', 'false'))

# Whether to group issues and PRs by ZenHub epics.
SHOW_EPICS = strtobool(os.environ.get('SHOW_EPICS', 'false'))


def main():
    gapi = github.api(GITHUB_TOKEN)
    zapi = zenhub.api(ZENHUB_TOKEN)

    # Build the full dependency graph from ZenHub's per-workspace API.
    print('Fetching graph')
    dg = nx.compose_all([
        zenhub.get_dependency_graph(zapi, workspace_id, repos)
        for (workspace_id, repos) in WORKSPACES.items()
        if len(repos) > 0
    ])

    print('Rendering DAG')

    if SHOW_EPICS:
        epics_issues = []
        for (workspace_id, repos) in WORKSPACES.items():
            if len(repos) > 0:
                epics_issues += zenhub.get_epics(zapi, workspace_id, repos)
        epics_issues = set(epics_issues)

        epics_mapping = github.download_issues(gapi, [gh_ref for (_, gh_ref) in epics_issues], REPOS)
        epics_mapping = {k: v for (k, v) in epics_mapping.items() if v.state != 'closed'}
        issues_by_epic = {}
        for (i, ((repo_id, epic_id), epic)) in enumerate(epics_mapping.items()):
            workspace_id = [
                workspace_id
                for (workspace_id, repos) in WORKSPACES.items()
                if repo_id in repos
            ][0]
            epic_id = [
                id for (id, gh_ref) in epics_issues
                if gh_ref == (repo_id, epic_id)
            ][0]
            issues = set(zenhub.get_epic_issues(zapi, workspace_id, epic_id))
            issues_by_epic[epic] = issues
            for i in issues:
                # zapi.dependencies only returns nodes that have some connection,
                # but we'd like to show all issues from epics even if they are
                # disconnected.
                dg.add_node(i)

    if len(TERMINATE_AT) > 0:
        # Look up the repo IDs for the given terminating issues.
        reverse_repos = {v:k for k,v in REPOS.items()}
        terminate_at = [x.split('#') for x in TERMINATE_AT]
        terminate_at = set([(reverse_repos[tuple(r.split('/', 1))], int(i)) for (r, i) in terminate_at])

        # Replace the graph with the subgraph that only includes the terminating
        # issues and their ancestors.
        ancestors = [nx.ancestors(dg, n) for n in terminate_at]
        dg = nx.subgraph(dg, terminate_at.union(*ancestors))

    # Fetch the issues within the graph.
    mapping = github.download_issues(gapi, dg.nodes, REPOS)

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

    if len(ONLY_INCLUDE) > 0 and ONLY_INCLUDE.issubset(SUPPORTED_CATEGORIES):
        # Insert direct edges for all transitive paths in the graph. This creates edges
        # between target issues that were not previously directly connected, but were
        # "reachable".
        tc = nx.transitive_closure_dag(dg)

        # Remove non-target issues. This also removes their involved edges, leaving behind
        # the transitive closure of the target issues.
        tc.remove_nodes_from([n for n in dg.nodes if not n.any_cat(ONLY_INCLUDE)])

        # Reduce to the minimum number of edges representing the same transitive paths.
        # This is unique for a DAG.
        dg = nx.transitive_reduction(tc)

    if not INCLUDE_FINISHED:
        # Identify the disconnected subgraphs.
        subgraphs = [dg.subgraph(c) for c in nx.connected_components(dg.to_undirected())]

        # Identify subgraphs comprised entirely of closed issues.
        ignore = [g for g in subgraphs if all([n.state == 'closed' for n in g])]

        # Remove fully-closed subgraphs.
        if len(ignore) > 0:
            dg.remove_nodes_from(nx.compose_all(ignore))

    # Prune nodes that are not downstream of any open issues.
    if cats(PRUNE_FINISHED).issubset(SUPPORTED_CATEGORIES):
        closed_targets = [n for n in dg.nodes if n.any_cat(cats(PRUNE_FINISHED)) and n.state == 'closed']
        for target in closed_targets:
            # Check that the target (and by extension its ancestors) wasn't already
            # removed for being the ancestor of another closed target.
            if target in dg:
                ancestors = nx.ancestors(dg, target)
                if all(n.state == 'closed' for n in ancestors):
                    # Only prune ancestors, not the closed target node, so that
                    # we see the most recently-closed target nodes in the DAG.
                    dg.remove_nodes_from(ancestors)

    elif PRUNE_FINISHED in ['true', 'all']:
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
        elif n.waiting_on_review:
            attrs['class'] = 'needs-review'
            attrs['fillcolor'] = '#dfc150'
        elif n.is_committed or n.is_in_progress:
            attrs['class'] = 'committed'
            attrs['fillcolor'] = '#a6cfff'
        else:
            attrs['class'] = 'open'
            attrs['fillcolor'] = '#c2e0c6'
        attrs['penwidth'] = 2 if n in do_next else 1
        if n.is_target:
            attrs['shape'] = 'folder'
        elif n.is_pr:
            attrs['shape'] = 'component'
        else:
            attrs['shape'] = 'box'
        attrs['style'] = 'filled'
        if n.url:
            attrs['URL'] = n.url
            attrs['target'] = '_blank'

    ag = nx.nx_agraph.to_agraph(dg)

    clusters = 0
    if SHOW_MILESTONES:
        # Identify milestone nbunches
        milestones = {n.milestone: [] for n in dg}
        for m in milestones:
            milestones[m] = [n for n in dg if n.milestone == m]
        if None in milestones:
            del milestones[None]
        for (milestone, nodes) in milestones.items():
            ag.add_subgraph(nodes, 'cluster_%d' % clusters, label=milestone, color='blue')
            clusters += 1

    if SHOW_EPICS:
        for (epic, issues) in issues_by_epic.items():
            issues = [n for n in dg if (n.repo_id, n.issue_number) in issues]
            if issues:
                ag.add_subgraph(issues, 'cluster_%d' % clusters, label=epic.title, color='blue')
                clusters += 1

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
