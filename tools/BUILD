subinclude("//:version")

# This target is meant to be used as the default pex tool for this plugin. It relies on the released artifact which might
# not exist yet and as such, the hash sums won't be available too. To solve this a test will be run to guarantee that the
# hashes below will match the ones of the artifact once released.
remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/v{VERSION}/please_pex-{VERSION}-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = [
        "00dbdbbe6634a1b48684ee65b9b8ae08f5b4b8e65c65030b69d0cef8ee483613",
        "0a696dcd57609e654780ee86d6d449168214e42f344b5df0cfb7490f2150b902",
        "56140b95306fb70957868160c42b39c47b568c030030d4d724beb92a0000b899",
        "d405f108d718ef4cf4091915512ec9a7da62a6e6d784fdb95d6b5d5a39efa48c",
        "e123a33809781e7ed2ecd35850f29b375fde1e443a39b3b6adc5ef7ae256376a",
    ],
    binary = True,
    visibility = ["PUBLIC"],
)

remote_file(
    name = "arcat",
    url = f"https://github.com/please-build/arcat/releases/download/v1.0.0/arcat-1.0.0-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = ["6705304dde3cf358d7b8f5a034dfcc8242474b76d0e439b2f39a7a99f8612749"],
    binary = True,
    visibility = ["PUBLIC"],
)
