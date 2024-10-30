#!/usr/bin/env bash
set -efuo pipefail

views=${*:-core wallet tfl halo2 zf}

for view in ${views}
do
    echo Generating ${view} DAG...
    DAG_VIEW=${view} \
    SHOW_MILESTONES=true \
    SHOW_EPICS=true \
    GITHUB_TOKEN="$(cat GITHUB_TOKEN)" \
    ZENHUB_TOKEN="$(cat ZENHUB_TOKEN)" \
    uv run ./zcash-issue-dag.py
done
