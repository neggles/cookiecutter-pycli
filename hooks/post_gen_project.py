#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def remove_file(filename: str) -> None:
    Path.cwd().joinpath(filename).unlink()


def main():
    if "{{ cookiecutter.choose_a_license }}" == "Not open source":
        remove_file("LICENSE.md")

    subprocess.check_call(["git", "init"])
    subprocess.check_call(["git", "commit", "-a", "-m", "init"])
    subprocess.check_call(["git", "tag", "v{{ cookiecutter.project_version }}"])
    subprocess.check_call(["python3", "-m", "virtualenv", ".venv", "--download"])
    subprocess.check_call(
        [
            "source",
            ".venv/bin/activate",
            "&&",
            "python",
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
            "setuptools",
            "wheel",
            "&&",
            "pip",
            "install",
            "--editable",
            ".[dev]",
            "&&",
            "python",
            "-m",
            "setuptools_scm",
        ]
    )

    print(SUCCESS + "Project initialized! nice." + TERMINATOR)
    sys.exit(0)


if __name__ == "__main__":
    main()
