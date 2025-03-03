class Repo(object):
    def __init__(self, name, gh_id, zh_id):
        self.name = name
        self.gh_id = gh_id
        self.zh_id = zh_id

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

ZIP32 = Repo(('zcash', 'zip32'), 141066493, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTY2MzAy')
LIBRUSTZCASH = Repo(('zcash', 'librustzcash'), 85334928, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTg5MDU1NTE')
ZCASH_ANDROID_WALLET_SDK = Repo(('Electric-Coin-Company', 'zcash-android-wallet-sdk'), 151763639, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTg5MDI4MjE')
ZCASH_LIGHT_CLIENT_FFI = Repo(('Electric-Coin-Company', 'zcash-light-client-ffi'), 439137887, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzMTMwNjcy')
ZCASH_SWIFT_WALLET_SDK = Repo(('Electric-Coin-Company', 'zcash-swift-wallet-sdk'), 185480114, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTg5MDU1NjE')
ZASHI_ANDROID = Repo(('Electric-Coin-Company', 'zashi-android'), 390808594, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzMDEwMTMw')
ZASHI_IOS = Repo(('Electric-Coin-Company', 'zashi-ios'), 387551125, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzMDEwMTI5')

HALO2_REPOS = [
    Repo(('zcash', 'halo2'), 290019239, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyNzg1NDUx'),
    Repo(('zcash', 'pasta_curves'), 344239327, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyOTI3Njg2'),
]

CORE_REPOS = [
    Repo(('zcash', 'zcash'), 26987049, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvOTc3ODc2NQ'),
    Repo(('zcash', 'zips'), 47279130, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMjIwMzQwMDY'),
    Repo(('zcash', 'incrementalmerkletree'), 48303644, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzMDcwMDc5'),
    LIBRUSTZCASH,
    Repo(('zcash', 'zcash-test-vectors'), 133857578, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyOTMxNTEx'),
    Repo(('zcash', 'sapling-crypto'), 111058300, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTY3ODY4'),
    Repo(('zcash', 'orchard'), 305835578, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyODU2MzA2'),
    Repo(('zcash', 'wallet'), 863610221, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTM0MzU3MjQ0'),
    ZIP32,
] + HALO2_REPOS

TFL_REPOS = [
    Repo(('Electric-Coin-Company', 'tfl-book'), 642135348, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTE2NDQz'),
    Repo(('Electric-Coin-Company', 'zebra-tfl'), 725179873, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTY0OTEy'),
    Repo(('Electric-Coin-Company', 'simtfl'), 695805989, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTQ0MTk5'),
]

ANDROID_REPOS = [
    ZASHI_ANDROID,
    ZCASH_ANDROID_WALLET_SDK,
    Repo(('Electric-Coin-Company', 'zashi'), 719178328, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTYwOTgw'),
]

IOS_REPOS = [
    ZASHI_IOS,
    ZCASH_SWIFT_WALLET_SDK,
    Repo(('Electric-Coin-Company', 'MnemonicSwift'), 270825987, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyNzk3Mzg0'),
    ZCASH_LIGHT_CLIENT_FFI,
    Repo(('Electric-Coin-Company', 'zashi'), 719178328, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTYwOTgw'),
]

WALLET_REPOS = [
    LIBRUSTZCASH,
    Repo(('zcash', 'lightwalletd'), 159714694, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTg5MDU1NzE'),
] + ANDROID_REPOS + IOS_REPOS

ECC_REPOS = CORE_REPOS + TFL_REPOS + WALLET_REPOS + [
    Repo(('Electric-Coin-Company', 'infrastructure'), 65419597, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMjIwNTA1NjY'),
]

ZF_REPOS = [
    Repo(('ZcashFoundation', 'zebra'), 205255683, None),
    Repo(('ZcashFoundation', 'redjubjub'), 225479018, None),
    Repo(('ZcashFoundation', 'ed25519-zebra'), 235651437, None),
    Repo(('ZcashFoundation', 'zcash_script'), 279422254, None),
]

ZF_FROST_REPOS = [
    Repo(('ZcashFoundation', 'frost'), 437862440, None),
]

ZCASHD_DEPRECATION_REPOS = [
    Repo(('zcash', 'zcash'), 26987049, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvOTc3ODc2NQ'),
    Repo(('zcash', 'zips'), 47279130, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMjIwMzQwMDY'),
    LIBRUSTZCASH,
    Repo(('zcash', 'wallet'), 863610221, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTM0MzU3MjQ0'),
    Repo(('zcash', 'lightwalletd'), 159714694, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTg5MDU1NzE'),
]

ZALLET_REPOS = [
    Repo(('zcash', 'zips'), 47279130, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMjIwMzQwMDY'),
    Repo(('zcash', 'incrementalmerkletree'), 48303644, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzMDcwMDc5'),
    LIBRUSTZCASH,
    Repo(('zcash', 'zcash-test-vectors'), 133857578, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyOTMxNTEx'),
    Repo(('zcash', 'sapling-crypto'), 111058300, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMzOTY3ODY4'),
    Repo(('zcash', 'orchard'), 305835578, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTMyODU2MzA2'),
    Repo(('ZcashFoundation', 'zcash_script'), 279422254, None),
    Repo(('zcash', 'wallet'), 863610221, 'Z2lkOi8vcmFwdG9yL1JlcG9zaXRvcnkvMTM0MzU3MjQ0'),
    ZIP32,
] + HALO2_REPOS

POOL_DEPRECATION_REPOS = CORE_REPOS + WALLET_REPOS

ALL_REPOS = set(ECC_REPOS + ZF_REPOS + ZF_FROST_REPOS + ZCASHD_DEPRECATION_REPOS)
