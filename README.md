# Zcash Developers Hub

This is the source repository for the Zcash Developers Hub website: https://zcash.github.io/developers/

For now, this repo hosts the script used to generate ECC's development dependency graph, and a workflow that generates and hosts it.

## Setup

This project uses `uv` for dependency management: https://docs.astral.sh/uv/
It also depends on the Graphviz library; for Debian-based distros, install the
`libgraphviz-dev` package.

After installing `uv`, run `uv sync`.

### Authorization Tokens

The scripts provided by this project require two files:

- `GITHUB_TOKEN`: a GitHub API token with permission to read the necessary repositories.
- `ZENHUB_TOKEN`: a ZenHub REST API token. (Not a GraphQL token.)

After generating each token, paste the literal contents into the associated file. There is a
`.gitignore` which ignores these files to ensure they are not committed. Be careful to avoid
that editor temporary files or any copies or renames of these files aren't committed.

You can generate a GitHub token with [this url](https://github.com/settings/tokens/new). This
token should not have any excess authority; it only needs public read access! Make sure all of
those extra capability checkboxes are unchecked.

The DAG script depends upon GraphQL APIs for GitHub which can be generated using
`./gen-schema.sh`.

## Generating DAGs

The simplest way to generate one or more DAGs is to use `./gen-dag.sh` script. This takes
a list of DAGs to render as arguments (default: `core wallet tfl halo2 zf`).

Alternatively, the `zcash-issue-dag.py` script supports several configuration options
supplied as environment variables:

- `DAG_VIEW=[core|halo2|tfl|wallet|wallet-ios|wallet-android|zf]`: The DAG to render (default: `core`).
- `SHOW_MILESTONES=[true|false]`: Whether or not to render GitHub milestones as boxes (default: `false`).
- `SHOW_EPICS=[true|false]`: Whether or not to render ZenHub epics as boxes (default: `false`).
- `INCLUDE_FINISHED=[true|false]`: Whether or not to include closed issues with no open blockers (default: `false`).

Example command:

```
DAG_VIEW=core SHOW_MILESTONES=false uv run ./zcash-issue-dag.py
```
