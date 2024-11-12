subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.5.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "001a60589ee54723324ca8a3bb22e047aae1538daa1cf302b2da1fa2bf54c467",  # please_pex-1.5.1-darwin_amd64
        "5e9e327678b4f8926071951321af7457d2dddbf5c03f5776ff25f1c52f2b0f23",  # please_pex-1.5.1-darwin_arm64
        "579c9659c60b7187989ee9e559e2623bc84bd0ae533f74f575a6124a5e2e8bf1",  # please_pex-1.5.1-freebsd_amd64
        "3520d6d0a1611ae8c64c0db8eb1d67bb533f150e85d5220a3b8088f1136c2e16",  # please_pex-1.5.1-linux_amd64
        "9be649b5f2872548559b5314a557c18967ede42ceb19725af1c728b9d4b94cd7",  # please_pex-1.5.1-linux_arm64
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
