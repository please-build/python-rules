_PLEASE_PEX_VERSION = "3.0.4"

remote_file(
    name = "please_pex",
    url = f"https://github.com/please-build/python-rules/releases/download/please_pex-v{_PLEASE_PEX_VERSION}/please_pex-{_PLEASE_PEX_VERSION}-{CONFIG.OS}_{CONFIG.ARCH}",
    hashes = [
        "e236a10133048084df3203708a180d1dcedfe879445c4febb4899cf71a73c676",  # darwin_amd64
        "2cc35b876a1e652f5b12d966c0eaae55ee94259ae5d3dbc7a9e6aedd142c9d53",  # darwin_arm64
        "b9154a8066e50db226d01e7bfbe120dd3a20045b3cef5bab52400d14fc2e08b9",  # freebsd_amd64
        "68b7beadc8199cbfd6057fb3ba86a027b0c4c677bbbf1e46e1f584cbb37dde11",  # linux_amd64
        "626170fb50e71536c54bb00ea56c44c3c2f8eaa556cf128b1568b7f01d6a201d",  # linux_arm64
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
