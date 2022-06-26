#!/usr/bin/env bash

echo "Setting up {{ cookiecutter.project_name }} repo in $(pwd)"
git init
git add --quiet .
git commit --quiet --message "Initial commit"
git tag v{{ cookiecutter.project_version }}

echo "Creating python virtualenv"
/usr/bin/env python3 -m virtualenv .venv
source .venv/bin/activate

echo "Updating pip and setuptools"
pip install --upgrade --quiet pip setuptools wheel

echo "Installing package in dev mode..."
pip install --editable '.[dev]'
python -m setuptools_scm

exit 0
