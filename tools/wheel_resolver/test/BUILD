subinclude("//build_defs:python")

python_test(
    name = "lib_test",
    srcs = ["test.py"],
    deps = ["//tools/wheel_resolver/src/wheel_tags:tags"],
)

gentest(
    name = "e2e_test",
    data = ["//tools/wheel_resolver/src:wheel_resolver"],
    no_test_output = True,
    test_cmd = "PKG=tensorflow; export OUTS=$PKG.whl; $DATA --package \"$PKG\"; \
                if [[ -f \"$PKG\".whl ]]; then exit 0; else exit 1; fi;",
)

gentest(
    name = "test_resolve_protobuf",
    data = ["//tools/wheel_resolver"],
    no_test_output = True,
    test_cmd = "true",
    srcs = [":protobuf"],
)

python_wheel(
    name = "protobuf",
    outs = ["google"],
    version = "3.18.1",
    deps = [
        "//third_party/python:six",
    ],
)
