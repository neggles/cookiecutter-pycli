#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import compile as re_compile
from sys import exit as sys_exit

re_module = re_compile(r"^[a-z][\w]+$")

module_name = "{{ cookiecutter.__package_name }}"

if bool(re_module.match(module_name)) is not True:
    print(f"ERROR: {module_name} is not a valid Python module name!")

    # exits with status 1 to indicate failure
    sys_exit(1)
