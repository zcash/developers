class Repo(object):
    def __init__(self, name, gh_id):
        self.name = name
        self.gh_id = gh_id

    def __repr__(self):
        if self.name:
            repo = self.name
            # Shorten the representation of long repo names.
            if repo[0] == 'Electric-Coin-Company':
                repo = ('ECC', repo[1])
            return '/'.join(repo)
        else:
            return 'Unknown (%d)' % self.gh_id

    def __eq__(self, other):
        return self.gh_id == other.gh_id

    def __hash__(self):
        return hash(self.gh_id)


# To get the GitHub ID of a repo, see <https://stackoverflow.com/a/47223479/393146>.

HALO2_REPOS = [
    Repo(('zcash', 'halo2'), 290019239),
    Repo(('zcash', 'pasta_curves'), 344239327),
]

CORE_REPOS = [
    Repo(('zcash', 'zcash'), 26987049),
    Repo(('zcash', 'zips'), 47279130),
    Repo(('zcash', 'incrementalmerkletree'), 48303644),
    Repo(('zcash', 'librustzcash'), 85334928),
    Repo(('zcash-hackworks', 'zcash-test-vectors'), 133857578),
    Repo(('zcash', 'sapling-crypto'), 111058300),
    Repo(('zcash', 'orchard'), 305835578),
] + HALO2_REPOS

TFL_REPOS = [
    Repo(('Electric-Coin-Company', 'tfl-book'), 642135348),
    Repo(('Electric-Coin-Company', 'zebra-tfl'), 725179873),
    Repo(('zcash', 'simtfl'), 695805989),
]

ANDROID_REPOS = [
    Repo(('Electric-Coin-Company', 'zashi-android'), 390808594),
    Repo(('Electric-Coin-Company', 'zcash-android-wallet-sdk'), 151763639),
    Repo(('Electric-Coin-Company', 'zashi'), 719178328),
]

IOS_REPOS = [
    Repo(('Electric-Coin-Company', 'zashi-ios'), 387551125),
    Repo(('Electric-Coin-Company', 'zcash-swift-wallet-sdk'), 185480114),
    Repo(('Electric-Coin-Company', 'MnemonicSwift'), 270825987),
    Repo(('Electric-Coin-Company', 'zcash-light-client-ffi'), 439137887),
    Repo(('Electric-Coin-Company', 'zashi'), 719178328),
]

WALLET_REPOS = [
    Repo(('zcash', 'librustzcash'), 85334928),
    Repo(('zcash', 'lightwalletd'), 159714694),
] + ANDROID_REPOS + IOS_REPOS

ECC_REPOS = CORE_REPOS + TFL_REPOS + WALLET_REPOS + [
    Repo(('Electric-Coin-Company', 'infrastructure'), 65419597),
]

ZF_REPOS = [
    Repo(('ZcashFoundation', 'zebra'), 205255683),
    Repo(('ZcashFoundation', 'redjubjub'), 225479018),
    Repo(('ZcashFoundation', 'ed25519-zebra'), 235651437),
    Repo(('ZcashFoundation', 'zcash_script'), 279422254),
]

ZF_FROST_REPOS = [
    Repo(('ZcashFoundation', 'frost'), 437862440),
]

ZCASHD_DEPRECATION_REPOS = [
    Repo(('zcash', 'zcash'), 26987049),
    Repo(('zcash', 'zips'), 47279130),
    Repo(('zcash', 'librustzcash'), 85334928),
    Repo(('zcash', 'wallet'), 863610221),
    Repo(('zcash', 'lightwalletd'), 159714694),
]

POOL_DEPRECATION_REPOS = CORE_REPOS + WALLET_REPOS

ALL_REPOS = set(ECC_REPOS + ZF_REPOS + ZF_FROST_REPOS + ZCASHD_DEPRECATION_REPOS)
