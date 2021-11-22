// Package main implements please_pex, which builds runnable Python zip files for us.
package main

import (
	"gopkg.in/op/go-logging.v1"

	cli "github.com/peterebden/go-cli-init/v5/flags"
	"github.com/please-build/python-rules/tools/please_pex/pex"
)

var log = logging.MustGetLogger("please_pex")

var opts = struct {
	Usage              string
	Out                string       `short:"o" long:"out" env:"OUT" description:"Output file"`
	EntryPoint         string       `short:"e" long:"entry_point" env:"SRC" description:"Entry point to pex file"`
	ModuleDir          string       `short:"m" long:"module_dir" description:"Python module dir to implicitly load modules from"`
	TestSrcs           []string     `long:"test_srcs" env:"SRCS" env-delim:" " description:"Test source files"`
	Interpreter        string       `short:"i" long:"interpreter" env:"TOOLS_INTERPRETER" description:"Python interpreter to use"`
	TestRunner         string       `short:"r" long:"test_runner" default:"unittest" description:"Test runner to use"`
	Shebang            string       `short:"s" long:"shebang" description:"Explicitly set shebang to this"`
	Stamp              string       `long:"stamp" description:"Unique value used to derive cache directory for pex"`
	InterpreterOptions string       `long:"interpreter_options" description:"Options-string to pass to the python interpreter"`
	Test               bool         `short:"t" long:"test" description:"True if we're to build a test"`
	Debug              pex.Debugger `short:"d" long:"debug" optional:"true" optional-value:"pdb" choice:"pdb" choice:"debugpy" description:"Debugger to generate a debugging pex"`
	Site               bool         `short:"S" long:"site" description:"Allow the pex to import site at startup"`
	ZipSafe            bool         `long:"zip_safe" description:"Marks this pex as zip-safe"`
}{
	Usage: `
please_pex is a tool to create .pex files for Python.

These are not really pex files any more, they are just zip files (which Python supports
out of the box). They still have essentially the same approach of containing all the
dependent code as a self-contained self-executable environment.
`,
}

func main() {
	cli.ParseFlagsOrDie("please_pex", &opts, nil)
	w := pex.NewWriter(
		opts.EntryPoint, opts.Interpreter, opts.InterpreterOptions, opts.Stamp,
		opts.ZipSafe, !opts.Site)
	if opts.Shebang != "" {
		w.SetShebang(opts.Shebang, opts.InterpreterOptions)
	}
	if opts.Test {
		w.SetTest(opts.TestSrcs, opts.TestRunner)
	}
	if len(opts.Debug) > 0 {
		w.SetDebugger(opts.Debug)
	}
	if err := w.Write(opts.Out, opts.ModuleDir); err != nil {
		log.Fatalf("%s", err)
	}
}
