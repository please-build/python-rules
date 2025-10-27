_PLEASE_PEX_VERSION = "2.2.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "f0ef8ac72f2a815d37b1dc8f8dfc060c3625ca59e5a5e5fe3603fce3ff40ae7f",  # darwin_amd64
        "f88d51555c83f4b926ed04a6daa28f7abb103d83e7e04172de5876b199b683c1",  # darwin_arm64
        "51faa96067ab087ed9edae95a3f7dddc33707337e5e392bf4f1ab1d72e465c78",  # freebsd_amd64
        "2f1000dfe13e65337fe03ea5929f1402aa2a5adcca30684a99131ab31917212a",  # linux_amd64
        "7dcf5b9a5faa318cbdc1a35e3419a38944231e3ba3ad70948abb611ed9676c5d",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
