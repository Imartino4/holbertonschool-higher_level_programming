#!/usr/bin/python3
""" This module contain is_kind_of_class function
    which evaluate if the object is an instance of a class or an instance 
    of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """Receives an object and a class, and returns
    True if the object belongs to the class, and False if not """

    if isinstance(obj, a_class):
        return True
    return False
