subinclude("//build_defs:python")

go_binary(
    name = "pex_main",
    srcs = ["pex_main.go"],
    deps = [
        "//third_party/go:cli-init",
        "//third_party/go:go-logging.v1",
        "//tools/please_pex/pex",
    ],
)

# Combine all the Python dependencies into one zipfile and concatenate them
# onto the binary.
genrule(
    name = "please_pex",
    srcs = [
        ":pex_main",
    ],
    outs = ["please_pex"],
    binary = True,
    cmd = [
        '"$TOOL" z -d -i . -o "$OUTS" --preamble_file $(location :pex_main)',
    ],
    tools = ["//tools:arcat"],
    visibility = ["PUBLIC"],
    labels = ["hlink:plz-out/package"],
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
