#!/usr/bin/python3
""" 
Module to add integers
add_integer receives two number as parameters
"""


def add_integer(a, b=98):
    """ Function to add a + b
    Args:
        a: must be int or float
        b: must be int ot float

    Return:
        add_integer(5, 7)
        12
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError(a must be an integer)
    a = int(a)
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError(b must be an integer)
    b = int(b)
    return a + b
