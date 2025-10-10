version = "3.12.11"
release = "20251007"

remote_file(
    name = "download",
    url = f"https://github.com/indygreg/python-build-standalone/releases/download/{release}/cpython-{version}+{release}-x86_64_v2-unknown-linux-gnu-pgo+lto-full.tar.zst",
    hashes = ["36fd10710d73b46d9a0a0ff81536306faefe51855936ec53840f39a6b5394cba"],
)

genrule(
    name = "cpython",
    srcs = [":download"],
    outs = [f"python-{version}"],
    cmd = [
        "tar --strip-components=1 -xf $SRCS",
        "mv install $OUTS",
    ],
    binary = True,
    entry_points = {
        "python": f"python-{version}/bin/python3",
    },
    visibility = ["PUBLIC"],
)
