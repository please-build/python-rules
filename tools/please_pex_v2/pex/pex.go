// Package pex implements construction of .pex files in Go.
// For performance reasons we've ultimately abandoned doing this in Python;
// we were ultimately not using pex for much at construction time and
// we already have most of what we need in Go via jarcat.
package pex

import (
	"bytes"
	"embed"
	"fmt"
	"log"
	"os"
	"path"
	"path/filepath"
	"strings"
)

const testRunnersDir = "test_runners"
const debuggersDir = "debuggers"

type Debugger string

const (
	Pdb     Debugger = "pdb"
	Debugpy Debugger = "debugpy"
)

//go:embed *.py
//go:embed test_runners/*.py
//go:embed debuggers/*.py
var files embed.FS

// A Writer implements writing a .pex file in various steps.
type Writer struct {
	zipSafe          bool
	noSite           bool
	shebang          string
	realEntryPoint   string
	pexStamp         string
	testSrcs         []string
	testRunner       string
	customTestRunner string
	debugger         string
}

// NewWriter constructs a new Writer.
func NewWriter(entryPoint, interpreter, options, stamp string, zipSafe bool) *Writer {
	pw := &Writer{
		zipSafe:        zipSafe,
		realEntryPoint: toPythonPath(entryPoint),
		pexStamp:       stamp,
	}
	return pw
}

// SetTest sets this Writer to write tests using the given sources.
// This overrides the entry point given earlier.
func (pw *Writer) SetTest(srcs []string, testRunner string) {
	pw.realEntryPoint = "pex_test_main"
	pw.testSrcs = srcs

	switch testRunner {
	case "pytest":
		pw.testRunner = filepath.Join(testRunnersDir, "pytest.py")
	case "behave":
		pw.testRunner = filepath.Join(testRunnersDir, "behave.py")
	case "unittest":
		pw.testRunner = filepath.Join(testRunnersDir, "unittest.py")
	default:
		if !strings.ContainsRune(testRunner, '.') {
			panic("Custom test runner '" + testRunner + "' is invalid; must contain at least one dot")
		}
		pw.testRunner = filepath.Join(testRunnersDir, "custom.py")
		pw.customTestRunner = testRunner
	}
}

func (pw *Writer) SetDebugger(debugger Debugger) {
	pw.pexStamp = "debug"

	switch debugger {
	case "pdb":
		pw.debugger = filepath.Join(debuggersDir, "pdb.py")
	case "debugpy":
		pw.debugger = filepath.Join(debuggersDir, "debugpy.py")
	default:
		log.Fatalf("Unknown debugger: %s", debugger)
	}
}

func appendByteArrayToFile(name string, data []byte, perm os.FileMode) error {
	f, err := os.OpenFile(name, os.O_APPEND|os.O_WRONLY|os.O_CREATE, perm)
	if err != nil {
		return err
	}
	_, err = f.Write(data)
	if err1 := f.Close(); err1 != nil && err == nil {
		err = err1
	}
	return err
}

// Write writes the pex to the given output file.
func (pw *Writer) Write(out, moduleDir string) error {
	// Create file
	f, err := os.Create("__main__.py")
	fmt.Printf("Created __main__.py\n")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	// Write pex_main.py with some templating.
	b := mustRead("pex_main.py")
	b = bytes.Replace(b, []byte("__MODULE_DIR__"), []byte(strings.ReplaceAll(moduleDir, ".", "/")), 1)
	b = bytes.Replace(b, []byte("__ENTRY_POINT__"), []byte(pw.realEntryPoint), 1)
	b = bytes.Replace(b, []byte("__ZIP_SAFE__"), []byte(pythonBool(pw.zipSafe)), 1)
	b = bytes.Replace(b, []byte("__PEX_STAMP__"), []byte(pw.pexStamp), 1)

	if len(pw.testSrcs) != 0 {
		// If we're writing a test, we append pex_test_main.py to it.
		b2 := mustRead("pex_test_main.py")
		b2 = bytes.Replace(b2, []byte("__TEST_NAMES__"), []byte(strings.Join(pw.testSrcs, ",")), 1)
		b = append(b, b2...)
		// It also needs an appropriate test runner.
		b = append(b, bytes.Replace(mustRead(pw.testRunner), []byte("__TEST_RUNNER__"), []byte(pw.customTestRunner), 1)...)
	}

	if len(pw.debugger) > 0 {
		b = append(b, mustRead(pw.debugger)...)
	}

	b = append(b, mustRead("pex_run.py")...)

	return appendByteArrayToFile("__main__.py", b, 0644)
}

// pythonBool returns a Python bool representation of a Go bool.
func pythonBool(b bool) string { //nolint:unused
	if b {
		return "True"
	}
	return "False"
}

// toPythonPath converts a normal path to a Python import path.
func toPythonPath(p string) string {
	ext := path.Ext(p)
	return strings.ReplaceAll(p[:len(p)-len(ext)], "/", ".")
}

// mustRead reads the given file from the embedded set. It dies on error.
func mustRead(filename string) []byte {
	b, err := files.ReadFile(filename)
	if err != nil {
		panic(err)
	}
	return b
}
