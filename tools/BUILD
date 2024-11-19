subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.5.5"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "bc430ad8f1b1ae5516490a26758d3e8efc65da64112ba69ecc79aa0251b4794e",  # please_pex-1.5.5-darwin_amd64
        "28865fc2f67e406f6544aef7fe2ba334d3fac3096ed54df4a270390c220db240",  # please_pex-1.5.5-darwin_arm64
        "1b47c2211b736891129f64659ef8f92afdb626477ca4ce428b808b3c6ce5d7ba",  # please_pex-1.5.5-freebsd_amd64
        "772068a245d6c19f082ea5f53a3ea9201f7c169c6ed225e8ddbf6e8092752f22",  # please_pex-1.5.5-linux_amd64
        "cdc04adcca95fd915328887083c50c38029409b5210c4a90bc81145b049002fe",  # please_pex-1.5.5-linux_arm64
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
