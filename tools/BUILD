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
