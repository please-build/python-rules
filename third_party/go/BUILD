subinclude("//build_defs:archs", "///go//build_defs:go")

go_toolchain(
    name = "toolchain",
    hashes = [
        "b770812aef17d7b2ea406588e2b97689e9557aac7e646fe76218b216e2c51406",  # darwin_arm64
        "ffd070acf59f054e8691b838f274d540572db0bd09654af851e4e76ab88403dc",  # darwin_amd64
        "905a297f19ead44780548933e0ff1a1b86e8327bb459e92f9c0012569f76f5e3",  # linux_amd64
        "2c2252902b87ba605fdc0b12b4c860fe6553c0c5483c12cc471756ebdd8249fe",  # freebsd_amd64
    ],
    architectures = SUPPORTED_ARCHS,
    strip_srcs = CONFIG.BUILD_CONFIG != "dbg",
    version = "1.23.0",
)

go_module(
    name = "go-logging.v1",
    licences = ["BSD-3-Clause"],
    module = "gopkg.in/op/go-logging.v1",
    version = "v1.0.0-20160211212156-b2cb9fa56473",
    visibility = ["PUBLIC"],
)

go_module(
    name = "testify",
    install = [
        "assert",
        "require",
    ],
    licences = ["MIT"],
    module = "github.com/stretchr/testify",
    version = "v1.7.0",
    visibility = ["PUBLIC"],
    deps = [
        ":difflib",
        ":spew",
        ":yaml",
    ],
)

go_module(
    name = "difflib",
    install = ["difflib"],
    licences = ["BSD-3-Clause"],
    module = "github.com/pmezard/go-difflib",
    version = "v1.0.0",
    visibility = ["PUBLIC"],
)

go_module(
    name = "spew",
    install = ["spew"],
    licences = ["ISC"],
    module = "github.com/davecgh/go-spew",
    patch = "spew_omit_empty.patch",
    version = "v1.1.1",
    visibility = ["PUBLIC"],
)

go_module(
    name = "yaml",
    licences = ["MIT"],
    module = "gopkg.in/yaml.v3",
    version = "v3.0.0-20210107192922-496545a6307b",
    visibility = ["PUBLIC"],
)

go_module(
    name = "cli-init",
    install = ["..."],
    module = "github.com/peterebden/go-cli-init/v5",
    version = "v5.1.0",
    licences = ["Apache-2.0"],
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
    licences = ["BSD-3-Clause"],
    version = "v0.0.0-20210823070655-63515b42dcdf",
)
