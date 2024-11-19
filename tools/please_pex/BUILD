subinclude("//build_defs:python", "///go//build_defs:go")

go_binary(
    name = "pex_main",
    srcs = ["pex_main.go"],
    deps = [
        "///third_party/go/github.com_peterebden_go-cli-init_v5//flags",
        "///third_party/go/github.com_peterebden_go-cli-init_v5//logging",
        "///third_party/go/gopkg.in_op_go-logging.v1//:go-logging.v1",
        "//tools/please_pex/pex",
    ],
)

# Combine all the Python dependencies into one zipfile and concatenate them
# onto the binary.
genrule(
    name = "please_pex",
    srcs = {
        "bootstraps": [
            "//third_party/python:coverage",
            "//third_party/python:portalocker",
            "//third_party/python:pytest",
            "//third_party/python:xmlrunner",
            "//third_party/python:behave",
        ],
        "main": [":pex_main"],
    },
    outs = ["please_pex"],
    binary = True,
    cmd = [
        'for i in $SRCS_BOOTSTRAPS; do if echo "$i" | grep -q \'\\.pex$\'; then "$TOOL" x -o . "$i"; rm -f "$i"; fi; done',
        "rm -f third_party/python/__*_main__.py*",
        # Have to make sure these exist.
        "touch third_party/__init__.py third_party/python/__init__.py",
        "touch tools/__init__.py tools/please_pex/__init__.py",
        "mv third_party/python/* .bootstrap",
        # A little cleanup.
        "rm -rf third_party .bootstrap/xmlrunner/extra .bootstrap/coverage/htmlfiles .bootstrap/.*.pex.zip",
        '"$TOOL" z -d -i .bootstrap -o "$OUTS" --preamble_file $(location :pex_main)',
    ],
    tools = [CONFIG.ARCAT_TOOL],
    visibility = ["PUBLIC"],
)

python_test(
    name = "pex_test",
    srcs = ["pex_test.py"],
)

python_test(
    name = "pex_import_test",
    srcs = ["pex_import_test.py"],
    deps = [
        "//third_party/python:dateutil",
        "//third_party/python:requests",
    ],
)
