_PLEASE_PEX_VERSION = "3.0.0"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "bb593d2c594a03c1ce92a948c56704b7adeb46b6eab1643678d1d2fd6d4cc6e4",  # darwin_amd64
        "affed12bef63b96f6582de04135f0ce524b1b87de19a07e05b4bdbee5e4aba8f",  # darwin_arm64
        "16453328e690ec5b850777d8796e0a5290994a59e841cdd6485979ae416ddeeb",  # freebsd_amd64
        "82792c5494fc6fe2c202890d5bf779bfd627083ca1b663d17d386bbc5212a023",  # linux_amd64
        "35661a9ca52b8807f0b0dcf68c6859a1692a6b8b79b27df3e29c324674de06cb",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
