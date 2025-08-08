#!/usr/bin/env python3

# Git repo commit graph generator.
# Author: jack@electriccoin.co
# Last updated: 2025-07-22

import networkx as nx

from str2bool import str2bool as strtobool
import os
from textwrap import wrap
from urllib.parse import urlparse

from helpers import github
from helpers.repos import LIBRUSTZCASH

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')

def cats(s):
    return set([x.strip() for x in s.split(',')]) - set([''])

# If set, removes all commits that are not ancestors of the given commits.
# This can be used to render a sub-graph focused on one area.
#
# Format is COMMIT_ID[,COMMIT_ID[, ..]]
TERMINATE_AT = cats(os.environ.get('TERMINATE_AT', ''))


def main():
    gapi = github.api(GITHUB_TOKEN)

    repo = LIBRUSTZCASH

    # Build the full dependency graph from ZenHub's per-workspace API.
    print('Fetching graph')
    dg = github.get_commit_graph(gapi, repo)

    print('Rendering DAG')

    if len(TERMINATE_AT) > 0:
        # Replace the graph with the subgraph that only includes the terminating
        # commits and their ancestors.
        terminate_at = set([n for n in dg.nodes if n.oid in TERMINATE_AT])
        ancestors = [nx.ancestors(dg, n) for n in terminate_at]
        dg = nx.subgraph(dg, terminate_at.union(*ancestors))

    # Apply style annotations.
    for n in dg:
        attrs = dg.nodes[n]
        if n.message_headline:
            attrs['label'] = '\n'.join(['%s' % n] + wrap(n.message_headline, 25))
        if n.is_unreviewed():
            attrs['class'] = 'needs-review'
            attrs['fillcolor'] = '#dfc150'
        else:
            attrs['class'] = 'open'
            attrs['fillcolor'] = '#c2e0c6'
        attrs['penwidth'] = 1 #2 if n in do_next else 1
        if n.is_merge:
            attrs['shape'] = 'component'
        else:
            attrs['shape'] = 'box'
            attrs['style'] = 'filled'
        if n.url:
            attrs['URL'] = n.url
            attrs['target'] = '_blank'

    ag = nx.nx_agraph.to_agraph(dg)

    # Draw the result!
    ag.graph_attr['rankdir'] = 'BT'
    ag.graph_attr['stylesheet'] = 'zcash-dag.css'
    ag.layout(prog='dot')
    os.makedirs('public', exist_ok=True)
    ag.draw('public/git-%s-dag.svg' % repo.name[1])

    # Render the HTML version!
    with open('public/git-%s-dag.svg' % repo.name[1]) as f:
        svg_data = f.read()
    svg_start = svg_data.find('<svg')
    html_data = '''<!DOCTYPE html>
<html>
  <head>
    <title>%s Git DAG</title>

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
''' % (repo, svg_data[svg_start:])
    with open('public/git-%s-dag.html' % repo.name[1], 'w') as f:
        f.write(html_data)


if __name__ == '__main__':
    if GITHUB_TOKEN:
        main()
    else:
        print('Please set the GITHUB_TOKEN environment variables.')
