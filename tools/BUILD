subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.6.2"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "589c9d77fa54aea5adea372f5278f33de33d8112268303a9e3a3380208b980a2",  # please_pex-1.6.2-darwin_amd64
        "78ee04052e02049ef22a3ba6e43b271c9451fa015a62c48ac9d4bee1df823861",  # please_pex-1.6.2-darwin_arm64
        "3c7d02badab7a996cbbf4b22b464faf4a6dfe34604a77456eb32c7966b5b5221",  # please_pex-1.6.2-freebsd_amd64
        "2f52070285ecdad4861a3dd048b4cc9e6ce850ab7090441d9de3577c9bcb3811",  # please_pex-1.6.2-linux_amd64
        "4410d53faa1b914e2e0ac08dee3d7352ff5e151c67574b85bcc9ea6b68ec67a1",  # please_pex-1.6.2-linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)

# This target is only intended for use during plugin development. Its only purpose is to break the
# mutual dependency between please_pex and the python_wheels in the bootstrap pex, which prevents
# PexTool from being set to //tools/please_pex in order to test changes to please_pex.
#
# See .plzconfig.tool_test for more details.
filegroup(
    name = "please_pex_dev",
    srcs = ["please_pex_dev"],
    binary = True,
    labels = ["manual"],
    visibility = ["PUBLIC"],
)
