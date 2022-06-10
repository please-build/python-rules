subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "0.1.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = [
        "3aa6d8b295bf99797e723bb7a5740de63351f091c64da65fd7ffa0b2c7ea5ce0", # linux_amd64
        "575c065da0053e75e69d6a684b42cd07f775dd2ace9f4b5d26feb37766788587", # linux_arm64
        "d1e58c872bd451eff6afe21513a99ef02e502097bf548c8d7382c2f2c900aef7", # darwin_amd64
        "db72e816085c03160310c18c6a1c6442a2c2e051fba31a7f05b848b0a0efdc77", # darwin_arm64
        "c31cb4ad4e60200de92fd0bf0cebba0a72f4ec0b8ffe56754c7ac2a867e10ed6", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
