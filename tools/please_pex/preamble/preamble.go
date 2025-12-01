// Package preamble is the Go interface to the .pex preamble format.
package preamble

import (
	"fmt"
	"strings"
)

// ConfigPath is the zip file member within the .pex archive containing the .pex preamble
// configuration. It is typically the first member of the archive (for performance reasons), but
// does not necessarily have to be.
const ConfigPath = ".bootstrap/PLZ_PREAMBLE_CONFIG"

// Verbosity represents a logging level supported by the .pex preamble.
type Verbosity string

const (
	LogTrace Verbosity = "trace"
	LogDebug           = "debug"
	LogInfo            = "info"
	LogWarn            = "warn"
	LogError           = "error"
	LogFatal           = "fatal"
)

// UnmarshalFlag parses a string representation of a logging level and returns its corresponding
// constant.
func (v *Verbosity) UnmarshalFlag(in string) error {
	switch strings.ToLower(in) {
	case "trace":
		*v = LogTrace
		return nil
	case "debug":
		*v = LogDebug
		return nil
	case "info":
		*v = LogInfo
		return nil
	case "warn":
		*v = LogWarn
		return nil
	case "error":
		*v = LogError
		return nil
	case "fatal":
		*v = LogFatal
		return nil
	}
	return fmt.Errorf("invalid preamble logging level '%s'", in)
}

// Config represents a .pex preamble configuration.
type Config struct {
	// Verbosity controls the preamble's minimum log level. It may be overridden at run time by the
	// value of the PLZ_PEX_PREAMBLE_VERBOSITY environment variable.
	Verbosity Verbosity `json:"verbosity,omitempty"`

	// Interpreters is a list of relative or absolute paths to Python interpreters that the preamble
	// should attempt to invoke in the order in which they are given. The preamble duplicates the
	// actions of the shell when attempting to locate an interpreter with a relative path that does not
	// contain a forward slash.
	Interpreters []string `json:"interpreters"`

	// InterpreterArgs is a list of command line arguments that the preamble should pass to the Python
	// interpreters when attempting to invoke them.
	InterpreterArgs []string `json:"interpreter_args,omitempty"`
}
