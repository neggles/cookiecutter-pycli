#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess
from pathlib import Path

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;31m [WARNING]:"
INFO = "\x1b[1;33m [INFO]:"
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]:"


def remove_file(filename: str) -> None:
    Path.cwd().joinpath(filename).unlink(missing_ok=True)


def confirm(message: str) -> bool:
    answer = ""
    while answer.lower not in ["y", "n"]:
        answer = input(f"{HINT} {message} [y/n]: {TERMINATOR}").lower()
    return answer == "y"


def main():
    if "{{ cookiecutter.choose_a_license }}" == "Not open source":
        remove_file("LICENSE.md")

    print(f"{INFO} Preparing repository... {TERMINATOR}")
    try:
        subprocess.check_call(["/usr/bin/env", "bash", ".setup.sh"])
    except subprocess.CalledProcessError as e:
        print(f"{WARNING}Failed to run .setup.sh: {TERMINATOR}\n{e}")
        if not confirm("Continue anyway?"):
            print(f"{WARNING} OK, giving up... {TERMINATOR}")
            sys.exit(1)
        print(f"{INFO} Continuing... {TERMINATOR}")

    print(f"{INFO} Removing setup files... {TERMINATOR}")
    remove_file(".setup.sh")

    print(f"{SUCCESS} Project setup complete. {TERMINATOR}")
    sys.exit(0)


if __name__ == "__main__":
    main()
