_PLEASE_PEX_VERSION = "3.0.3"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "391c852222d62959f1f4b609232853ee547490265077610aec5edc8e6db7e0e4",  # darwin_amd64
        "4c9f79a94acaf0610d66689a9f5dcd46bb0bf3a826e134ded0ba6a2d465f4461",  # darwin_arm64
        "7be3f36aec819a4d694244d556c8f4a6085f5d4b5816dd67d6bed1865190d27e",  # freebsd_amd64
        "fc22dbf09065dad56052dfddcd3be0b5a6c455d2055e3accae2e6d34bd6956ea",  # linux_amd64
        "23c61aec2ce9364b99fd1525ec6e797bb5771bbf3fa0bad1518cafb9d29bb8a3",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
