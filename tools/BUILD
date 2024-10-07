subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.3.5"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "38d885c02c069fd9b1376c81c047c24c4823699e82d7be9334e79f9ee4732341", # please_pex-1.3.5-darwin_amd64
        "b3746c69b7e406517eafa96c5b56729fe56a11ab35b48093f66c7bdf65592d43", # please_pex-1.3.5-darwin_arm64
        "ab2f2403f45251882e9407715e2b12b1d87ff9df00cb10daa2ad47b201083da2", # please_pex-1.3.5-freebsd_amd64
        "4b82a1fe8fb40ff072f25cb115be5fae89f2bab383e23ee61432451c82443257", # please_pex-1.3.5-linux_amd64
        "eb1728c545266fe0d050b52ffa0a7b99fb7f28fe7510142515d7189f4589ac26", # please_pex-1.3.5-linux_arm64
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
