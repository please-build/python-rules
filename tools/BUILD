subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.1.1"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "a104df6685a0dc000f53846c8b6b3380f644d41fd323ebe9812c6240d2c06f40", # linux_amd64
        "636e8644811ddc1aa97c16c2f73fc62beb07410bd6f1bdad9d99fee1a717b161", # linux_arm64
        "a26b9cff54fd640fb5381d998b55fe82a74a2fad5c43c61c4de2a415e6597cf3", # darwin_amd64
        "27687b388e362c3572b7133c691e9272fb7107e8f48069c534585a57c27e8289", # darwin_arm64
        "4aab777b9bb6969cbcab6b1d94924c320097f38da262d554749aa05601b37a26", # freebsd_amd64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
