subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.6.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "0d6eb076ec37023a8f708b1f4516d7cb960be824115a110fb41b97083e14bbab",  # please_pex-1.6.0-darwin_amd64
        "c41ee9db0224b257ced02b91823d03eeaa67748a2567cd47b5bf1c09ba930359",  # please_pex-1.6.0-darwin_arm64
        "9f07d77c20dbb9f81c84d5ea636c88ec830b2cbd498e8c29553c83921ef444b2",  # please_pex-1.6.0-freebsd_amd64
        "d1e07210f4834b971a6e606e8952c4c33b7403f649f75b29f927d3676c29d3b4",  # please_pex-1.6.0-linux_amd64
        "160ed67502b7f2e71b08cde44439a3748852d663cfab42f82aece1666f3cef19",  # please_pex-1.6.0-linux_arm64
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
