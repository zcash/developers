import networkx as nx
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from github_schema import github_schema as schema
from helpers.repos import (
    CORE_REPOS,
    HALO2_REPOS,
    TFL_REPOS,
    WALLET_REPOS,
    ZALLET_REPOS,
    IOS_REPOS,
    ANDROID_REPOS,
    ECC_REPOS,
    ZF_REPOS,
    ZF_FROST_REPOS,
    ZCASHD_DEPRECATION_REPOS,
    POOL_DEPRECATION_REPOS,
    POOL_DEPRECATION_REPOS,
)

REPO_SETS = {
    'core': CORE_REPOS,
    'halo2': HALO2_REPOS,
    'tfl': TFL_REPOS,
    'wallet': WALLET_REPOS,
    'wallet-ios': IOS_REPOS,
    'wallet-android': ANDROID_REPOS,
    'zallet': ZALLET_REPOS,
    'ecc': ECC_REPOS,
    'zf': ZF_REPOS,
    'zf-frost': ZF_FROST_REPOS,
    'zf-devops': ZF_REPOS + ZF_FROST_REPOS,
    'zcashd-deprecation': ZCASHD_DEPRECATION_REPOS,
    'sprout-deprecation': POOL_DEPRECATION_REPOS,
    'transparent-deprecation': POOL_DEPRECATION_REPOS,
}


def api(token):
    return HTTPEndpoint(
        'https://api.github.com/graphql',
        {'Authorization': 'bearer %s' % token},
    )


class GitHubIssue:
    def __init__(self, repo, issue_number, data, REPOS):
        self.repo = repo
        self.issue_number = issue_number
        self.milestone = None
        self._REPOS = REPOS

        if data is not None:
            labels = [label['name'] for label in data['labels']['nodes']]
            self.title = data['title']
            self.labels = labels
            self.is_release = 'C-release' in labels
            self.is_target = 'C-target' in labels
            self.is_pr = 'merged' in data
            self.is_committed = 'S-committed' in labels
            self.is_in_progress = 'S-in-progress' in labels
            self.waiting_on_review = 'S-waiting-on-review' in labels
            self.url = data['url']
            self.state = 'closed' if data['state'] in ['CLOSED', 'MERGED'] else 'open'
            if 'milestone' in data and data['milestone']:
                self.milestone = data['milestone']['title']
        else:
            # If we can't fetch issue data, assume we don't care.
            self.title = ''
            self.labels = []
            self.url = None
            self.is_release = False
            self.is_target = False
            self.is_pr = False
            self.is_committed = False
            self.is_in_progress = False
            self.waiting_on_review = False
            self.state = 'closed'

    def __repr__(self):
        if self.repo in self._REPOS:
            return '%s#%d' % (self.repo, self.issue_number)
        else:
            return 'Unknown'

    def __eq__(self, other):
        return (self.repo, self.issue_number) == (other.repo, other.issue_number)

    def __hash__(self):
        return hash((self.repo, self.issue_number))

    def any_cat(self, categories):
        release_cat = self.is_release if 'releases' in categories else False
        targets_cat = self.is_target if 'targets' in categories else False
        return release_cat or targets_cat


def fetch_issues(op, issues):
    repos = set([repo for (repo, _) in issues])
    repos = {repo: [issue for (r, issue) in issues if r == repo] for repo in repos}

    for repo, issues in repos.items():
        conn = op.repository(
            owner=repo.name[0],
            name=repo.name[1],
            __alias__='repo%d' % repo.gh_id,
        )

        for issue in issues:
            res = conn.issue_or_pull_request(number=issue, __alias__='issue%d' % issue)
            for typ in [schema.Issue, schema.PullRequest]:
                node = res.__as__(typ)
                node.labels(first=50).nodes().name()
                node.state()
                node.milestone().title()
                node.title()
                node.url()
                if typ == schema.PullRequest:
                    node.merged()


# `nodes` is a list of `(Repo, issue_number)` tuples.
def download_issues(endpoint, nodes, REPOS):
    issues = [(repo, issue) for (repo, issue) in nodes if repo in REPOS]

    ret = {}

    # Ensure that any graph nodes from ZenHub that are not in the repos we care about have
    # default entries, to simplify subsequent graph manipulation code.
    for repo, issue in [(repo, issue) for (repo, issue) in nodes if repo not in REPOS]:
        ret[(repo, issue)] = GitHubIssue(repo, issue, None, REPOS)

    def chunks(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    for issues in chunks(issues, 50):
        op = Operation(schema.Query)
        fetch_issues(op, issues)

        d = endpoint(op)
        data = op + d

        for repo, issue in issues:
            repo_data = data['repo%d' % repo.gh_id]
            issue_key = 'issue%d' % issue
            # If GITHUB_TOKEN doesn't have permission to read from a particular private
            # repository in REPOS, GitHub returns an empty repo_data section.
            issue_data = repo_data[issue_key] if issue_key in repo_data else None
            ret[(repo, issue)] = GitHubIssue(repo, issue, issue_data, REPOS)

    return ret


def fetch_issues_with_labels(op, labels, repos):
    for (repo, (issue_cursor, pr_cursor)) in repos:
        conn = op.repository(
            owner=repo.name[0],
            name=repo.name[1],
            __alias__='repo%d' % repo.gh_id,
        )

        if issue_cursor != -1:
            issues = conn.issues(
                labels=labels,
                first=50,
                after=issue_cursor,
            )
            issues.nodes.number()
            issues.nodes.labels(first=50).nodes().name()
            issues.nodes.state()
            issues.nodes.milestone().title()
            issues.nodes.title()
            issues.nodes.url()
            issues.page_info.has_next_page()
            issues.page_info.end_cursor()

        if pr_cursor != -1:
            prs = conn.pull_requests(
                labels=labels,
                first=50,
                after=pr_cursor,
            )
            prs.nodes.number()
            prs.nodes.labels(first=50).nodes().name()
            prs.nodes.state()
            prs.nodes.milestone().title()
            prs.nodes.title()
            prs.nodes.url()
            prs.nodes.merged()
            prs.page_info.has_next_page()
            prs.page_info.end_cursor()


def download_issues_with_labels(endpoint, labels, REPOS):
    ret = {}
    repos = {repo: (None, None) for repo in REPOS}

    while True:
        op = Operation(schema.Query)
        fetch_issues_with_labels(op, labels, repos.items())

        d = endpoint(op)
        data = op + d

        done = []
        for (repo, (_, _)) in repos.items():
            repo_data = data['repo%d' % repo.gh_id]

            if hasattr(repo_data, 'issues'):
                for issue in repo_data.issues.nodes:
                    ret[(repo, issue.number)] = GitHubIssue(repo, issue.number, issue, REPOS)
                if repo_data.issues.page_info.has_next_page:
                    issue_cursor = repo_data.issues.page_info.end_cursor
                else:
                    issue_cursor = -1
            else:
                issue_cursor = -1

            if hasattr(repo_data, 'pull_requests'):
                for pr in repo_data.pull_requests.nodes:
                    ret[(repo, pr.number)] = GitHubIssue(repo, pr.number, pr, REPOS)
                if repo_data.pull_requests.page_info.has_next_page:
                    pr_cursor = repo_data.pull_requests.page_info.end_cursor
                else:
                    pr_cursor = -1
            else:
                pr_cursor = -1

            if issue_cursor == -1 and pr_cursor == -1:
                done.append(repo)
            else:
                repos[repo] = (issue_cursor, pr_cursor)

        for repo in done:
            del repos[repo]

        if len(repos) > 0:
            print('.', end='', flush=True)
        else:
            print()
            break

    return ret


class GitHubCommit:
    def __init__(self, commit, branch):
        self.oid = commit.oid
        self.branch = branch
        self.message_headline = commit.message_headline
        self.url = commit.url
        self.is_merge = len(commit.parents.nodes) > 1
        if 'signature' in commit:
            if 'is_valid' in commit.signature:
                self.signature_is_valid = commit.signature.is_valid
            else:
                self.signature_is_valid = None
            if 'signer' in commit.signature:
                self.signer = commit.signature.signer.login
            else:
                self.signer = None

    def __repr__(self):
        if self.branch is None:
            return '{:.7}'.format(self.oid)
        else:
            return '{:.7} ({})'.format(self.oid, self.branch)

    def __eq__(self, other):
        return self.oid == other.oid

    def __hash__(self):
        return hash(self.oid)

    def is_merge_from_webui(self):
        return self.is_merge and self.signer == 'web-flow' and self.signature_is_valid is True

    def is_unreviewed(self):
        return not self.is_merge_from_webui()


def fetch_commit_graph(op, repo):
    conn = op.repository(
        owner=repo.name[0],
        name=repo.name[1],
        __alias__='repo%d' % repo.gh_id,
    )

    branch = (
        conn.refs(
            ref_prefix='refs/heads/',
            order_by={'direction': 'DESC', 'field': 'TAG_COMMIT_DATE'},
            first=100,
        )
        .nodes()
        .__as__(schema.Ref)
    )
    branch.name()
    pr = branch.associated_pull_requests(first=10).nodes()
    pr.number()
    pr.state()

    target = branch.target().__as__(schema.Commit)
    commit = target.history(first=100).nodes().__as__(schema.Commit)

    commit.message_headline()
    commit.oid()
    commit.url()
    parent = commit.parents(first=2).nodes().__as__(schema.Commit)
    parent.oid()

    sig = commit.signature()
    sig.is_valid()
    sig.signer().login()


# Fetches the commit graph for the given `repo`.
def get_commit_graph(endpoint, repo):
    nodes = {}
    edges = []

    op = Operation(schema.Query)
    fetch_commit_graph(op, repo)

    d = endpoint(op)
    data = op + d

    repo_data = data['repo%d' % repo.gh_id]

    if hasattr(repo_data, 'refs') and hasattr(repo_data.refs, 'nodes'):
        for branch in repo_data.refs.nodes:
            if hasattr(branch.associated_pull_requests, 'nodes'):
                # Don't include undeleted branches in the DAG for closed PRs.
                if all([pr.state == 'CLOSED' for pr in branch.associated_pull_requests.nodes]):
                    continue

            if hasattr(branch.target.history, 'nodes'):
                for i, commit in enumerate(branch.target.history.nodes):
                    nodes[commit.oid] = GitHubCommit(commit, branch.name if i == 0 else None)
                    edges += [
                        (parent.oid, commit.oid)
                        for parent in commit.parents.nodes
                    ]

    dg = nx.relabel_nodes(nx.DiGraph(edges), nodes)

    dg.remove_nodes_from([n for n in dg.nodes if type(n) == str])

    return dg
