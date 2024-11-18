subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.5.3"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "3092c4ddab2265cbda66c752cd484d97a685d0f18016baaa124e493e1c98fda0",  # please_pex-1.5.3-darwin_amd64
        "06c8e6680718e16289325cea275aa9d14bb19ab0446337754635e76375779dc6",  # please_pex-1.5.3-darwin_arm64
        "bb8ed4b14e0d19e73e12905471be71370a1378f8395d846470a2b4b1be19440d",  # please_pex-1.5.3-freebsd_amd64
        "630e08fdff2af6727a6a9f785e2da708c879a8faff35df689b176d76ed9dae1e",  # please_pex-1.5.3-linux_amd64
        "6f65e36407f76706536a83c5156439738331ade8b2688d19c23270823ddab494",  # please_pex-1.5.3-linux_arm64
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
