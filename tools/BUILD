subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "0.1.1"

# remote_file(
#     name = "please_pex",
#     url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
#     hashes = [
#         "3aa6d8b295bf99797e723bb7a5740de63351f091c64da65fd7ffa0b2c7ea5ce0", # linux_amd64
#         "575c065da0053e75e69d6a684b42cd07f775dd2ace9f4b5d26feb37766788587", # linux_arm64
#         "d1e58c872bd451eff6afe21513a99ef02e502097bf548c8d7382c2f2c900aef7", # darwin_amd64
#         "db72e816085c03160310c18c6a1c6442a2c2e051fba31a7f05b848b0a0efdc77", # darwin_arm64
#         "c31cb4ad4e60200de92fd0bf0cebba0a72f4ec0b8ffe56754c7ac2a867e10ed6", # freebsd_amd64
#     ],
#     binary = True,
#     visibility = ["PUBLIC"],
# )

filegroup

remote_file(
    name = "wheel_resolver",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/wheel_resolver-{TOOLS_VERSION}-{CONFIG.HOSTOS}_{CONFIG.HOSTARCH}",
    hashes = [
        "40303befa469874270246082d914aef3f28461456a57e87caf6d0e0eb77d8629", # linux_amd64
        "0c84c59d4ddf1e6904775f7f931a883f98e964f2723a159cce6b8b7dc05f60f6", # linux_arm64
        "7c9244a886d06cc210c9776c0fa177730d9daebcc87db0ed885f215bf338238e", # darwin_amd64
        "e76d21dc9f1e4e4afaec6a91119884c34f640229cf0518b28c2af4ef3eb8f1d1", # darwin_arm64
        "1eec1f69154170702d2f42a88442309648d120ae5020b583a183d1b467767733", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
