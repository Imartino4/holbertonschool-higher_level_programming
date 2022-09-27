#!/usr/bin/python3
""" This module contains inherits_from function, which
    evaluates if the object is an instance of a class that 
    inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Evaluates if obj inherited from a_class"""

    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    return False
