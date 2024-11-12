version = "3.12.7"
release = "20241016"

remote_file(
    name = "download",
    url = f"https://github.com/indygreg/python-build-standalone/releases/download/{release}/cpython-{version}+{release}-x86_64_v2-unknown-linux-gnu-pgo+lto-full.tar.zst",
    hashes = ["98f64550d63fa2f5468b28482b1fed8aef33a70d81f1549b7a8be1a59db41d98"],
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
