subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.2.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "0fe1fa77055042d943a96a6e78da0fd61a7a1bd2e7c427de88cdda23e0d694aa", # linux_amd64
        "0f703712de5ad15455f12bf14b3b211bc9cd1967c224cb104e960909cd539d8d", # linux_arm64
        "82a05ae6c8cf0918c71f2ba18730969fcd9fe6d0ab0b7ba7750a2e4869e4a8a8", # darwin_amd64
        "4a821cab2ab74ab3bde3833628f5a69308f47e6ea5b02c7088527e61bd4abd2a", # darwin_arm64
        "792bf767355c9a671b1b258fde9fb72b036b0a2072a548a6cf1779ee954ee69d", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
