#!/usr/bin/python3
""" Pascal triangle """


def pascal_triangle(n):
    """Implement pascal triangle"""
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        if i != 0:
            pascal[i].append(1)
    return pascal
