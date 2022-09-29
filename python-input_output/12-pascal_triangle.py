#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """Implement pascal triangle"""
    if n <= 0:
        return []
    pascal = []
    for i in range (n):
        j = list(str(11 ** i))
        pascal += [j]
    return pascal
