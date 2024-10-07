subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.4.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "e38791658e9c877454124179a5cfcb2587e33870358dfa197eec2f238d3a2669", # please_pex-1.3.5-darwin_amd64
        "16add4748285f2900723b3cfec9576a3e7dea9a94ed08181b1677d98008509bf", # please_pex-1.3.5-darwin_arm64
        "8c0cfa52a1e1bac59394931f4ec1a8929315b9a80f7bd6caffea568df7c89e08", # please_pex-1.3.5-freebsd_amd64
        "d4d56b7afb6d3febfa9fcd5ecb19f63d088d947a83c49f8e81f07f6a1cb6756d", # please_pex-1.3.5-linux_amd64
        "da4ef7077953a8d1c9787c7f1c7b1963fc000b7c16206bdfcde14ae207af995b", # please_pex-1.3.5-linux_arm64
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
