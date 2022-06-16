#!/usr/bin/env bash

DAG_VIEW=wallet \
SHOW_MILESTONES=true \
#GITHUB_TOKEN=<INSERT> \
#ZENHUB_TOKEN=<INSERT> \
poetry run python ./zcash-issue-dag.py
