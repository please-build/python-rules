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

_WHEEL_RESOLVER_VERSION = "2.0.0"

remote_file(
    name = "wheel_resolver",
    url =
    f"https://github.com/please-build/python-rules/releases/download/wheel_resolver-v{_WHEEL_RESOLVER_VERSION}/wheel_resolver-{_WHEEL_RESOLVER_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "b48315ec1c6670faf7feb2a532a4d0cb104a03113525ef1799062d7576f66b36",  # darwin_amd64
        "70db6d2eb18ab915f555824a8f29fe0909bcf87db0b583a5d6ad3156a54a034a",  # darwin_arm64
        "d47802282b4acf1669a1d69531c69eb2dd3f0f069fd8e59d0c9aff946f7aff44",  # freebsd_amd64
        "6aa0304bde5ab5f68d3415fd8761f6684f5c88835791b0dbd12f909120d797c6",  # linux_amd64
        "09e340203aa88d4e9de7f61b044d1f29fb688abf3c8b7547f80ad6ca3e441495",  # linux_arm64
    ],
    binary = True,
    visibility = ["PUBLIC"],
)
