#!/usr/bin/env bash
set -euo pipefail

echo "Setting up {{ cookiecutter.project_name }} repo in $(pwd)"
git init
git add .
git commit --quiet --message "Initial commit"
git tag v{{ cookiecutter.project_version }}

function fail_and_exit {
    echo "Failed!"
    echo 'Please create a venv and install {{ cookiecutter.project_name }} manually.'
    echo "Cleaning up broken virtualenv..."
    rm -rf .venv
    exit 0
}

echo -n "Creating python virtualenv... "
if (/usr/bin/env python3 -m virtualenv .venv); then
    echo -n "Activating... "
    source .venv/bin/activate
    echo "Done."
else
    fail_and_exit
fi


echo -n "Updating pip and setuptools... "
if (pip install --quiet --require-virtualenv --upgrade pip setuptools wheel setuptools-scm); then
    echo "Done."
    echo 'Installing {{ cookiecutter.project_name }} in editable mode...'
    pip install --editable '.[dev]'
    python -m setuptools_scm
else
    fail_and_exit
fi

echo "Template deployment for {{ cookiecutter.project_name }} complete!"
exit 0
