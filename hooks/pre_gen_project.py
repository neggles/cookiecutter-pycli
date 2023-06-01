# -*- coding: utf-8 -*-

from re import compile as re_compile
from sys import exit as sys_exit

MODULE_REGEX = re_compile(r"^[_a-zA-Z][\w]+$")

module_name = r"{{cookiecutter.__package_name}}"

if not MODULE_REGEX.match(module_name):
    print(f"ERROR: {module_name} is not a valid Python module name!")

    # exits with status 1 to indicate failure
    sys_exit(1)
