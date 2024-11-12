#!/usr/bin/env python3

import os

from helpers import zenhub
from helpers.repos import ALL_REPOS

ZENHUB_TOKEN = os.environ.get('ZENHUB_TOKEN')


def main():
    zapi = zenhub.api(ZENHUB_TOKEN)

    repos = zenhub.get_workspace_repos(zapi, zenhub.WORKSPACE_SETS)

    for repo in repos:
        print(repo)


if __name__ == '__main__':
    if ZENHUB_TOKEN:
        main()
    else:
        print('Please set the ZENHUB_TOKEN environment variable.')
