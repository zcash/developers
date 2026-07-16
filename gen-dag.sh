#!/usr/bin/env bash
set -efuo pipefail

views=${*:-core wallet tfl halo2 zf}

for view in ${views}
do
    echo Generating ${view} DAG...
    DAG_VIEW=${view} \
    SHOW_MILESTONES=true \
    GITHUB_TOKEN="$(cat GITHUB_TOKEN)" \
    uv run ./zcash-issue-dag.py
done
