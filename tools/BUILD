_PLEASE_PEX_VERSION = "2.1.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "20a17c3e5b488d3c5a76701058a4a2253fcae64ca4d931b11b9f832ec772b355",  # darwin_amd64
        "38678696fed81a815fd722d92dd73a89517d6633eca9198be751b42c2e3ca5f1",  # darwin_arm64
        "51ff6051c5405a958a6c03f694ed98dfe89a3a4f56532e4ce5bb6cab70543f49",  # freebsd_amd64
        "2790c426a21d23beee34e931d9c08ea41c621e14a610addad4a2c99c8ce6a95c",  # linux_amd64
        "f8b1b6f28efd85f937c4576c17b2be33e0d30a49bc6ae97612cd48e0c749d5a2",  # linux_arm64
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
