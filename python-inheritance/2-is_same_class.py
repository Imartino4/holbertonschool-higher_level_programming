#!/usr/bin/python3
""" This module contain is_same_object function
    which evaluate if an instance belongs to a specified class
"""


def is_same_class(obj, a_class):
    """Receives an object and a class, and returns
    True if the object belongs to the class, and False if not """

    if type(obj) == a_class:
        return True
    return False
