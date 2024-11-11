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
