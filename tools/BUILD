_PLEASE_PEX_VERSION = "1.7.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "d8f518764c06e690ea1a4fb90fd532b00c15247cd7d8fb58562748df5b1a0db7",  # darwin_amd64
        "3a4ff1599c757d2dff4ed9a11e2efa429bb7e644fe8f6ee7191ae1dec903e57b",  # darwin_arm64
        "d06718efeaac6fac70f82d6a4321094d485cd9c8a295bc4168a9cf678ee6109e",  # freebsd_amd64
        "cc0b7d29d7c495a983f9f520fb9e625f6bde868d6c092b82df0764cdcd61e36b",  # linux_amd64
        "0018b5197281f9f8830d15c78c3913a068bfda7a92a72f5ff90e4af6c17115cd",  # linux_arm64
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
