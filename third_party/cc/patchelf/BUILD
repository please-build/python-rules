subinclude("///cc//build_defs:cc")

package(
    cc = {
        "default_dbg_cppflags": CONFIG.CC.DEFAULT_DBG_CPPFLAGS + ["-std=c++17"],
        "default_opt_cppflags": CONFIG.CC.DEFAULT_OPT_CPPFLAGS + ["-std=c++17"],
    },
)

_version = "0.18.0"

remote_file(
    name = "download",
    url = f"https://github.com/NixOS/patchelf/releases/download/{_version}/patchelf-{_version}.tar.bz2",
    extract = True,
    hashes = ["1952b2a782ba576279c211ee942e341748fdb44997f704dd53def46cd055470b"],
)

genrule(
    name = "extract",
    srcs = [":download"],
    outs = {
        "srcs": ["src/patchelf.cc"],
        "hdrs": [
            "src/elf.h",
            "src/patchelf.h",
        ],
    },
    cmd = f"for i in $OUTS; do install $PKG/patchelf-{_version}/$i $i; done",
)

cc_binary(
    name = "patchelf",
    srcs = [":extract|srcs"],
    hdrs = [":extract|hdrs"],
    visibility = ["//third_party/cc/cpython/..."],
)
