#!/bin/sh

# This script builds a tool release (i.e. an architecture-specific binary target
# in //tools) and reports its location to the actions/upload-artifact action so
# it can be uploaded as part of the release workflow.

if [ "$GITHUB_ACTIONS" != true ]; then
    echo "This script should only be executed on GitHub Actions runners." >&2
    exit 1
fi

target="$1"

./pleasew -v notice -p build "$target"
echo ARTIFACT_PATH="$(./pleasew query output $target)" >> $GITHUB_ENV
