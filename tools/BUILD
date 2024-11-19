subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.6.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "eaeca3305a584ceff873550cc3f00779ce69829d98c4793adf7a2467a9e227d0",  # please_pex-1.6.1-darwin_amd64
        "eb8c8230859393e2c7f964525c37f492d799808beddef3fe091b8c10e85125b3",  # please_pex-1.6.1-darwin_arm64
        "19d5118a6f99975fa17209b996abc47d0ae632135921df6d0e87619a6843828c",  # please_pex-1.6.1-freebsd_amd64
        "321bf379b953d4138e0c4ae15f0b129917d3f8174504f75c1f6bc5676b4eeb3b",  # please_pex-1.6.1-linux_amd64
        "226384ea7b9b9e06eb2a000655c7557ac4fb0542aba1d6ed7b26b21ea92d441e",  # please_pex-1.6.1-linux_arm64
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
