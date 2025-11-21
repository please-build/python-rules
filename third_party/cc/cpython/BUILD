# Nothing in here is actually used - we just need this to initialise CONFIG.PYTHON for this package.
subinclude("//build_defs:archs")

_python_build_standalone_release = "20251031"
_python_build_standalone_hashes = {
    "3.10.19": {
        "aarch64-apple-darwin": "24be196d33ee1b40393beff9df721ed596ec90b8be3f424122f1300f41a4a3b6",
        "aarch64-unknown-linux-gnu": "ed1840fa7baa762d3506c161ee1887c29c3603737058a22639cd88ed69e4be9d",
        "aarch64-unknown-linux-musl": "e2ddd1e8980ecba2221074b9e3fccd10d0fbf1994974250eb537b066a0879e04",
        "x86_64-apple-darwin": "5f3a156f063f4a6fa522b1ebb724a7554a67be32318b69041e83fd77a2bd761c",
        "x86_64_v2-unknown-linux-gnu": "e5fe6913158b40b5ac897897c51c5879cac2684c435bf217774200fb863c9660",
        "x86_64_v2-unknown-linux-musl": "487fb8581280403300076b89b575def54c8b40143a1d84ed75432a08b134a024",
    },
    "3.11.14": {
        "aarch64-apple-darwin": "3ee35ef147a7ec7b62e4d5686742959f5a8ea557724a9cd183e0532a71cf3221",
        "aarch64-unknown-linux-gnu": "ed1840fa7baa762d3506c161ee1887c29c3603737058a22639cd88ed69e4be9d",
        "aarch64-unknown-linux-musl": "45dc662a82dae8db5dd706ddb7440e52ae2d521056b183488e1ce436a19530f3",
        "x86_64-apple-darwin": "7d283bcbfaf0204b98d9d0f4eea216fc41220f67739d60b89fb91f88e551b8fb",
        "x86_64_v2-unknown-linux-gnu": "b8679afca4481dc382fa44cf467d87f4b3b89ed3aa956e1ac4280ca235dbe560",
        "x86_64_v2-unknown-linux-musl": "a28d67ca4d5d1277b260d5e5529ce99bcff503db76f9625375fb700056a424ca",
    },
    "3.12.12": {
        "aarch64-apple-darwin": "2539a9105e47237aa8caabeed20587778f4acf9c6c4b3fe77f9bc2fd320720d2",
        "aarch64-unknown-linux-gnu": "05fb2e3fb98efca19e7bc5740646e0639afc3b573f580384592c212b0a4cd8c3",
        "aarch64-unknown-linux-musl": "3c30908c00027ecbd80d5f90b6e45c57230e0d81de5f051104bb91072fa24c75",
        "x86_64-apple-darwin": "10538a63ce7aa4d0891a3181150159fb5d3b750470a638ef8255a25dc50b9961",
        "x86_64_v2-unknown-linux-gnu": "009534a3a6a0b78054fd9c93943d894a89a8ee3318501c92a0b9684e903bdda9",
        "x86_64_v2-unknown-linux-musl": "e795c4e4fb24874e36df58ff7af50fdfc3fdb5ebee73f60fb81eb1a5218a34f5",
    },
    "3.13.9": {
        "aarch64-apple-darwin": "6924bd5fbf74dba25cf733a91deebe313e91f26f261aec8c1d0dc4cb8a9d8738",
        "aarch64-unknown-linux-gnu": "0cbb7b12215e000224f0834543ab4ad02d88c9b772198e2ab80311aff6dbc294",
        "aarch64-unknown-linux-musl": "a7ddc8c5970971f533ca05edae9378638ba52de6054bd0e6399dafac7ba790a8",
        "x86_64-apple-darwin": "b79e2e45b38cf4c8743c61745fe33de95912866d8d81bd97ddff3477098420f9",
        "x86_64_v2-unknown-linux-gnu": "02e055d1168e926491d6ec35745d1be0ffaa60bae56ab4c44aafbffbdac9178c",
        "x86_64_v2-unknown-linux-musl": "85b219bb03abec4873ec53dc06039b71ff7500baaaa52903896b5e1e17a1911c",
    },
    "3.14.0": {
        "aarch64-apple-darwin": "4d37c50912b533913fe4a6f0239acb737d65dc6dad72096c4573b755c6b26712",
        "aarch64-unknown-linux-gnu": "04c0886b0fa9eecb9c2a768ae554c9a6b494ba9f60b1faefc2995d8e1ca2faff",
        "aarch64-unknown-linux-musl": "f2ba1c9dbf269e506efa367c0ce30b708d60487a182455fc087280cda76796f7",
        "x86_64-apple-darwin": "77d1edb6a69676cf8e6c2ced749daddf4d8aec179f3195ae0613aef2066abe81",
        "x86_64_v2-unknown-linux-gnu": "4e93f17a52447fc4f22c716322e9a86db83fc90449839d2e7a2c0338849b7a79",
        "x86_64_v2-unknown-linux-musl": "695ae14a62020773fb07b7a64f7e90c0163734c1839f8712277d7f82921c387d",
    },
}

_freebsd_ports_hashes = {
    "python310-3.10.19": "1e06d1552d0d7a377606a0855bd13926261d59dffd18eb9a60ec97f64860ffc9",
    "python311-3.11.14": "b371de2a4a4137f8176b118f24d328fc12e4e9280071f6282db1c182e083b6b2",
    "python312-3.12.12_2": "a2cb0fa91ff0b6ca7aea19466c2c779416a6cb1e6cb56b43c64e33237e207778",
    "python313-3.13.9": "6a43c25e8034f5ddc80d5c07e407df67c91e46c185e16be5851e94d34858fb48",
    "python314-3.14.0_1": "a6e1bd9f41c1bb500795679f5206a035b7c9228755c347bc078690111bb48ca4",
}

for minor in ["3.10", "3.11", "3.12", "3.13", "3.14"]:
    if CONFIG.OS == "freebsd":
        package = filter(lambda v: v.startswith("python" + minor.replace(".", "")), _freebsd_ports_hashes.keys())[0]

        download = remote_file(
            name = tag(f"cpython_{minor}", "download"),
            url = f"https://pkg.freebsd.org/FreeBSD:14:amd64/latest/All/{package}.pkg",
            hashes = [_freebsd_ports_hashes[package]],
        )

        genrule(
            name = f"cpython_{minor}",
            srcs = [download],
            outs = [f"python_{minor}"],
            cmd = [
                "mkdir $OUTS",
                "tar -C $OUTS -xf $SRCS --strip-components=3 /usr/local",
                # The contents of FreeBSD Ports packages are designed to be installed beneath /usr/local, so we'll have
                # to do some slightly hacky rpath editing to make sure the Python interpreter can find libpython3.x at
                # run time:
                f"$TOOLS_PATCHELF --set-rpath '$ORIGIN/../lib' $OUTS/bin/python{minor}",
            ],
            binary = True,
            entry_points = {
                "python": f"python_{minor}/bin/python{minor}",
            },
            tools = {
                "patchelf": "//third_party/cc/patchelf",
            },
            visibility = ["PUBLIC"],
        )
    else:
        arch = "aarch64" if CONFIG.ARCH == "arm64" else "x86_64" if CONFIG.OS == "darwin" else "x86_64_v2"
        os = "apple-darwin" if CONFIG.OS == "darwin" else "unknown-linux-musl" if "musl" in CONFIG.PYTHON.FEATURE_FLAGS else "unknown-linux-gnu"
        target = f"{arch}-{os}"
        version = filter(lambda v: v.startswith(f"{minor}."), _python_build_standalone_hashes.keys())[0]

        download = remote_file(
            name = tag(f"cpython_{minor}", "download"),
            url = "https://github.com/astral-sh/python-build-standalone/releases/download/%s/cpython-%s+%s-%s-install_only_stripped.tar.gz" % (
                _python_build_standalone_release,
                version,
                _python_build_standalone_release,
                target,
            ),
            hashes = [_python_build_standalone_hashes[version][target]],
        )

        genrule(
            name = f"cpython_{minor}",
            srcs = [download],
            outs = [f"python_{minor}"],
            cmd = [
                "tar -xf $SRCS",
                "mv python $OUTS",
            ],
            binary = True,
            entry_points = {
                "python": f"python_{minor}/bin/python3",
            },
            visibility = ["PUBLIC"],
        )
