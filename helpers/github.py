from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from github_schema import github_schema as schema

# To get the id of a repo, see <https://stackoverflow.com/a/47223479/393146>.

HALO2_REPOS = {
    290019239: ('zcash', 'halo2'),
    344239327: ('zcash', 'pasta_curves'),
}

CORE_REPOS = {
    26987049: ('zcash', 'zcash'),
    47279130: ('zcash', 'zips'),
    48303644: ('zcash', 'incrementalmerkletree'),
    85334928: ('zcash', 'librustzcash'),
    133857578: ('zcash-hackworks', 'zcash-test-vectors'),
    111058300: ('zcash', 'sapling-crypto'),
    **HALO2_REPOS,
    305835578: ('zcash', 'orchard'),
}

TFL_REPOS = {
    642135348: ('Electric-Coin-Company', 'tfl-book'),
    725179873: ('Electric-Coin-Company', 'zebra-tfl'),
    695805989: ('zcash', 'simtfl'),
}

ANDROID_REPOS = {
    390808594: ('Electric-Coin-Company', 'zashi-android'),
    151763639: ('Electric-Coin-Company', 'zcash-android-wallet-sdk'),
    719178328: ('Electric-Coin-Company', 'zashi'),
}

IOS_REPOS = {
    387551125: ('Electric-Coin-Company', 'zashi-ios'),
    185480114: ('Electric-Coin-Company', 'zcash-swift-wallet-sdk'),
    270825987: ('Electric-Coin-Company', 'MnemonicSwift'),
    439137887: ('Electric-Coin-Company', 'zcash-light-client-ffi'),
    719178328: ('Electric-Coin-Company', 'zashi'),
}

WALLET_REPOS = {
    85334928: ('zcash', 'librustzcash'),
    159714694: ('zcash', 'lightwalletd'),
    **ANDROID_REPOS,
    **IOS_REPOS,
}

ECC_REPOS = {
    **CORE_REPOS,
    **TFL_REPOS,
    **WALLET_REPOS,
    65419597: ('Electric-Coin-Company', 'infrastructure'),
}

ZF_REPOS = {
    205255683: ('ZcashFoundation', 'zebra'),
    225479018: ('ZcashFoundation', 'redjubjub'),
    235651437: ('ZcashFoundation', 'ed25519-zebra'),
    279422254: ('ZcashFoundation', 'zcash_script'),
}

ZF_FROST_REPOS = {
    437862440: ('ZcashFoundation', 'frost'),
}

ZCASHD_DEPRECATION_REPOS = {
    26987049: ('zcash', 'zcash'),
    47279130: ('zcash', 'zips'),
    85334928: ('zcash', 'librustzcash'),
    863610221: ('zcash', 'wallet'),
    159714694: ('zcash', 'lightwalletd'),
}

POOL_DEPRECATION_REPOS = {
    **CORE_REPOS,
    **WALLET_REPOS,
}

REPO_SETS = {
    'core': CORE_REPOS,
    'halo2': HALO2_REPOS,
    'tfl': TFL_REPOS,
    'wallet': WALLET_REPOS,
    'wallet-ios': IOS_REPOS,
    'wallet-android': ANDROID_REPOS,
    'ecc': ECC_REPOS,
    'zf': ZF_REPOS,
    'zf-frost': ZF_FROST_REPOS,
    'zf-devops': {**ZF_REPOS, **ZF_FROST_REPOS},
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
    def __init__(self, repo_id, issue_number, data, REPOS):
        self.repo_id = repo_id
        self.issue_number = issue_number
        self.milestone = None
        self._REPOS = REPOS

        if data is not None:
            labels = [label['name'] for label in data['labels']['nodes']]
            self.title = data['title']
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
            self.url = None
            self.is_release = False
            self.is_target = False
            self.is_pr = False
            self.is_committed = False
            self.is_in_progress = False
            self.waiting_on_review = False
            self.state = 'closed'

    def __repr__(self):
        if self.repo_id in self._REPOS:
            repo = self._REPOS[self.repo_id]
            # Shorten the representation of long repo names.
            if repo[0] == 'Electric-Coin-Company':
                repo = ('ECC', repo[1])
            repo = '/'.join(repo)
            return '%s#%d' % (repo, self.issue_number)
        else:
            return 'Unknown'

    def __eq__(self, other):
        return (self.repo_id, self.issue_number) == (other.repo_id, other.issue_number)

    def __hash__(self):
        return hash((self.repo_id, self.issue_number))

    def any_cat(self, categories):
        release_cat = self.is_release if 'releases' in categories else False
        targets_cat = self.is_target if 'targets' in categories else False
        return release_cat or targets_cat


def fetch_issues(op, issues, REPOS):
    repos = set([repo for (repo, _) in issues])
    repos = {repo: [issue for (r, issue) in issues if r == repo] for repo in repos}

    for repo, issues in repos.items():
        conn = op.repository(
            owner=REPOS[repo][0],
            name=REPOS[repo][1],
            __alias__='repo%d' % repo,
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
        fetch_issues(op, issues, REPOS)

        d = endpoint(op)
        data = op + d

        for repo, issue in issues:
            repo_data = data['repo%d' % repo]
            issue_key = 'issue%d' % issue
            # If GITHUB_TOKEN doesn't have permission to read from a particular private
            # repository in REPOS, GitHub returns an empty repo_data section.
            issue_data = repo_data[issue_key] if issue_key in repo_data else None
            ret[(repo, issue)] = GitHubIssue(repo, issue, issue_data, REPOS)

    return ret
