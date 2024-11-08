subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.4.2"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "bfcc0e8b7dbd35def6ffd5ed2966b2a93276107145a5e1f1cb49894b389dcc29", # please_pex-1.4.2-darwin_amd64
        "21a9445cb3882ce3639d9e610af778d10e05a2466d60c3904cf395f326364ee8", # please_pex-1.4.2-darwin_arm64
        "0325da3903ab41717dffbc84d1ff0c7ee0e24723e11588613a79dfac2bfcf674", # please_pex-1.4.2-freebsd_amd64
        "511c2275e5f08e365fbc44ef3c8b97d51fde6437a1aef362577ea5c3fb0535ba", # please_pex-1.4.2-linux_amd64
        "dc0ade93aa9ba4e0e0a91034bb4aa59ea377c836954a890e7014671b194eb96d", # please_pex-1.4.2-linux_arm64
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
