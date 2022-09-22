#!/usr/bin/python3
"""This module has a function which print a square"""


def print_square(size):
    """ print a square with '#'
        Args:
        size: int
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end ="")
        print()
