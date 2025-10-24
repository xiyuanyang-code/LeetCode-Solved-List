#!/bin/bash
git add .
PYTHON_SCRIPT="auto_commit.py"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Could not find '$PYTHON_SCRIPT'. Please ensure it's in the same directory."
    exit 1
fi

python "$PYTHON_SCRIPT"
exit $?