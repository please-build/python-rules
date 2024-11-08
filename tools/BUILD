subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.5.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "942125ca11b243dab446b7f84634c6b450722bace370f7dec87b98afefb2a0d0", # please_pex-1.5.0-darwin_amd64
        "6ad9b8d6fb89c90a67c1269f7af35f12d28bf629cd338bbebaed6621e3da2e7e", # please_pex-1.5.0-darwin_arm64
        "9ccaacbb37d65b209cb78038fff2238141994cd953e2d69a7cc539625d960b37", # please_pex-1.5.0-freebsd_amd64
        "b9b4d309dd39749b63cee5d3b360b6eebaa06a8cb8408964dacfbecfce31bf8f", # please_pex-1.5.0-linux_amd64
        "237c4718102d57e53641e482261ee462d8ba4bb75880dd0536b0c072a127f1a2", # please_pex-1.5.0-linux_arm64
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
