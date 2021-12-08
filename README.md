# Zcash Developers Hub

This is the source repository for the Zcash Developers Hub website: https://zcash.github.io/developers/

For now, this repo hosts the script used to generate ECC's development dependency graph, and a workflow that generates and hosts it.

## Generating DAGs

The `zcash-issue-dag.py` script has two required environment variables:

- `GITHUB_TOKEN`: a GitHub API token with permission to read the necessary repositories.
- `ZENHUB_TOKEN`: a ZenHub API token.

It also supports several configuration options, also supplied as environment variables:

- `DAG_VIEW=[core|wallet|zf]`: The DAG to render (default: `core`).
- `SHOW_MILESTONES=[true|false]`: Whether or not to render GitHub milestones as boxes (default: `false`).
- `INCLUDE_FINISHED=[true|false]`: Whether or not to include closed issues with no open blockers (default: `false`).

Here's an example script for easily running the DAG script:

```bash
#!/usr/bin/env bash
DAG_VIEW=core \
SHOW_MILESTONES=false \
GITHUB_TOKEN=<INSERT> \
ZENHUB_TOKEN=<INSERT> \
python ./zcash-issue-dag.py
```

