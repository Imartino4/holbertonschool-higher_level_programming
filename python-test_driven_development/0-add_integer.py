#!/usr/bin/python3
"""

    Module to add integers

"""


def add_integer(a, b=98):
    """
    Functino to add a + b
    arg(a, b) must be int or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError(a must be an integer)
    a = int(a)
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError(b must be an integer)
    b = int(b)
    return a + b
