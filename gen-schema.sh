#!/usr/bin/env bash
set -eu

uv run python3 -m sgqlc.introspection \
  --exclude-deprecated \
  --exclude-description \
  -H "Authorization: bearer $(cat GITHUB_TOKEN)" \
  https://api.github.com/graphql \
  github_schema.json

uv run sgqlc-codegen schema github_schema.json github_schema.py

uv run python3 -m sgqlc.introspection \
  --exclude-description \
  -H "Authorization: bearer $(cat ZENHUB_TOKEN)" \
  https://api.zenhub.com/public/graphql \
  zenhub_schema.json

uv run sgqlc-codegen schema zenhub_schema.json zenhub_schema.py
