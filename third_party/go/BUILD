subinclude("//build_defs:archs", "///go//build_defs:go")

go_toolchain(
    name = "toolchain",
    hashes = [
        "9c3c0124b01b5365f73a1489649f78f971ecf84844ad9ca58fde133096ddb61b",  # darwin_amd64
        "ebac39fd44fc22feed1bb519af431c84c55776e39b30f4fd62930da9c0cfd1e3",  # darwin_arm64
        "424a5618406800365fe3ad96a795fb55ce394bea3ff48eaf56d292bf7a916d1e",  # freebsd_amd64
        "999805bed7d9039ec3da1a53bfbcafc13e367da52aa823cb60b68ba22d44c616",  # linux_amd64
    ],
    install_std = False,
    architectures = SUPPORTED_ARCHS,
    strip_srcs = CONFIG.BUILD_CONFIG != "dbg",
    version = "1.22.6",
)

go_stdlib(
    name = "std",
    tags = [
        "netgo",
        "osusergo",
    ],
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
