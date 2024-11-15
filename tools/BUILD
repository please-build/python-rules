subinclude("//build_defs:version")

version(name = "version")

TOOLS_VERSION = "1.5.2"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/tools-v{TOOLS_VERSION}/please_pex-{TOOLS_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "82ab31cb55303cc030358533ec48e389b21f364eba48e521b37c023f25d9a53b",  # please_pex-1.5.2-darwin_amd64
        "d70925f71c1d51f317e68e83089d95583e0f56b4b3c6cd713f91a14435ff7c46",  # please_pex-1.5.2-darwin_arm64
        "3eb0ec2face2270d3bfee2ad00e34843c39dc497a61d82585974e62941edcb89",  # please_pex-1.5.2-freebsd_amd64
        "7137e9fa7d20dae02debe30108bfae3f3273353980a9f241c8586fb0f1ff2824",  # please_pex-1.5.2-linux_amd64
        "164f1bc7981ac63f2fd38d22a9b32f17ec156f0507ab74aae35fd19c4737f3e9",  # please_pex-1.5.2-linux_arm64
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
