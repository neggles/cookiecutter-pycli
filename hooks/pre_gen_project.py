#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import compile as re_compile
from sys import exit as sys_exit

MODULE_REGEX = re_compile(r"^[_a-zA-Z][_a-zA-Z0-9]+$")

# fmt: off
module_name = '{{ cookiecutter.__package_name }}'
# fmt: on

if not MODULE_REGEX.match(module_name):
    print(f"ERROR: {module_name} is not a valid Python module name!")

    # exits with status 1 to indicate failure
    sys_exit(1)
