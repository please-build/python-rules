subinclude("//build_defs:archs")

go_toolchain(
    name = "toolchain",
    hashes = [
        "da4e3e3c194bf9eed081de8842a157120ef44a7a8d7c820201adae7b0e28b20b",  # darwin_arm64
        "355bd544ce08d7d484d9d7de05a71b5c6f5bc10aa4b316688c2192aeb3dacfd1",  # darwin_amd64
        "6bf89fc4f5ad763871cf7eac80a2d594492de7a818303283f1366a7f6a30372d",  # linux_amd64
        "15c184c83d99441d719da201b26256455eee85a808747c404b4183e9aa6c64b4",  # freebsd_amd64
    ],
    architectures = SUPPORTED_ARCHS,
    strip_srcs = CONFIG.BUILD_CONFIG != "dbg",
    version = "1.17",
)

go_module(
    name = "go-logging.v1",
    licences = ["BSD-3-Clause"],
    module = "gopkg.in/op/go-logging.v1",
    version = "v1.0.0-20160211212156-b2cb9fa56473",
    visibility = ["PUBLIC"],
)

go_module(
    name = "cli-init",
    install = ["..."],
    module = "github.com/peterebden/go-cli-init/v5",
    version = "v5.1.0",
    visibility = ["PUBLIC"],
    deps = [
        ":go-flags",
        ":go-logging.v1",
        ":humanize",
        ":xcrypto",
    ],
)

go_module(
    name = "go-flags",
    licences = ["BSD-3-Clause"],
    module = "github.com/thought-machine/go-flags",
    version = "v1.6.0",
    visibility = ["PUBLIC"],
    deps = [":xsys"],
)

go_module(
    name = "humanize",
    licences = ["MIT"],
    module = "github.com/dustin/go-humanize",
    version = "v1.0.0",
    visibility = ["PUBLIC"],
)

go_module(
    name = "xcrypto",
    install = [
        "cast5",
        "curve25519",
        "curve25519/internal/field",
        "ed25519",
        "ssh/terminal",
    ],
    licences = ["BSD-3-Clause"],
    module = "golang.org/x/crypto",
    version = "v0.0.0-20210920023735-84f357641f63",
    visibility = ["PUBLIC"],
    deps = [":xterm"],
)

go_module(
    name = "xterm",
    licences = ["BSD-3-Clause"],
    module = "golang.org/x/term",
    version = "v0.0.0-20210615171337-6886f2dfbf5b",
    visibility = ["PUBLIC"],
    deps = [":xsys"],
)

go_module(
    name = "xsys",
    install = ["..."],
    module = "golang.org/x/sys",
    version = "v0.0.0-20210823070655-63515b42dcdf",
)
