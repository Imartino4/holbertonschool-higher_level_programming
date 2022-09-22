#!/usr/bin/python3
"""
This module include say_my_name function
which prints name and last_name given as argument
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
    first_name: string
    last_name: string

    Print: My name is <first name> <last name>
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    return print(f"My name is {first_name} {last_name}")
