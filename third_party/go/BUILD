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
    name = "deferred_regex",
    licences = ["Apache-2.0"],
    module = "github.com/peterebden/go-deferred-regex",
    version = "v1.0.0",
    visibility = ["PUBLIC"],
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
    name = "levenshtein",
    install = ["levenshtein"],
    licences = ["MIT"],
    module = "github.com/texttheater/golang-levenshtein",
    version = "v1.0.1",
    visibility = ["PUBLIC"],
)

go_module(
    name = "promptui",
    install = [
        "...",
    ],
    module = "github.com/manifoldco/promptui",
    version = "v0.7.0",
    deps = [
        ":ansiterm",
        ":readline",
    ],
)

go_module(
    name = "semver",
    install = ["semver"],
    licences = ["Apache-2.0"],
    module = "github.com/coreos/go-semver",
    version = "v0.3.0",
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
    name = "ansiterm",
    install = [
        "...",
    ],
    module = "github.com/juju/ansiterm",
    version = "720a0952cc2ac777afc295d9861263e2a4cf96a1",
    deps = [
        ":colorable",
        ":go-isatty",
        ":vtclean",
    ],
)

go_module(
    name = "xsys",
    install = ["..."],
    module = "golang.org/x/sys",
    version = "v0.0.0-20210823070655-63515b42dcdf",
)

go_module(
    name = "readline",
    licences = ["MIT"],
    module = "github.com/chzyer/readline",
    version = "v0.0.0-20180603132655-2972be24d48e",
    visibility = ["PUBLIC"],
)

go_module(
    name = "colorable",
    licences = ["MIT"],
    module = "github.com/mattn/go-colorable",
    version = "v0.1.8",
    visibility = ["PUBLIC"],
    deps = [":go-isatty"],
)

go_module(
    name = "go-isatty",
    licences = ["MIT"],
    module = "github.com/mattn/go-isatty",
    version = "v0.0.14",
    visibility = ["PUBLIC"],
    deps = [":xsys"],
)

go_module(
    name = "vtclean",
    licences = ["MIT"],
    module = "github.com/lunixbochs/vtclean",
    version = "v1.0.0",
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
    #patch = "spew_omit_empty.patch",
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
