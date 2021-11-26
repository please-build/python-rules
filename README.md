# Python rules

This repo is a plugin that provides python rules for the [Please](https://please.build) build system.

## Basic usage

```python
# BUILD
# This adds the plugin to your project
github_repo(
    name = "python_rules",
    repo = "please-build/python-rules",
    revision = "<Some git tag, commit, or other reference>",
)

# src/main/python/build/please/foo/BUILD
# This defines a python library that can be depended on by other python rules
python_library(
    name = "foo",
    srcs = ["foo.py"],
    visibility = ["//src/test/python/build/please/..."]
)

# src/test/python/build/please/foo/BUILD
# A test for the above library
python_test(
    name = "foo_test",
    srcs = ["foo_test.py"],
    deps = [
        "//src/main/python/build/please/foo",
    ]
)

# src/main/python/build/please/foo/BUILD
# This produces an executable pex file
python_binary(
    name = "pybin",
    main = "pybin.py",
    deps = ["//src/main/python/build/please/foo"]
)
```

Add the following to your `.plzconfig`
```
[Parse]
PreloadSubincludes = @python_rules//build_defs:python
```

Alternatively, if you are not using python everywhere, you can simply put `subinclude("@python_rules//build_defs:python")` at the top of individual BUILD files as needed.

## Configuration

Plugins are configured under a Plugin heading like so:
```
[Plugin "python"]
DefaultInterpreter = python3
```

The available configuration options are:

[Plugin "python"]
InterpreterOptions = -b -s
DefaultInterpreter = python3
PexTool = @self//tools/please_pex
TestRunner = unittest
ModuleDir = third_party.python
WheelRepo = https://pypi.org/pypi
WheelNameScheme = None
WheelTool = @self//tools/wheel_resolver
TestRunnerDeps = @self//third_party/python:unittest_bootstrap
PipTool = 
DefaultPipRepo
UsePypi
PipFlags
DisableVendorFlags
