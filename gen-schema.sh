#!/usr/bin/env bash
set -eu

uv run python3 -m sgqlc.introspection \
  --exclude-deprecated \
  --exclude-description \
  -H "Authorization: bearer $(cat GITHUB_TOKEN)" \
  https://api.github.com/graphql \
  github_schema.json

uv run sgqlc-codegen schema github_schema.json github_schema.py
