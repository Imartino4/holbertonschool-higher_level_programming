#!/usr/bin/python3
""" Operate with matrix """


def matrix_divided(matrix, div):
    """ This function divide each element of the matrix by 0
    Args:
        matrix: list of list, each element must be an int or float
        div: int or float, except 0
    Return:
        a new matrix
    """
    
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) != int and type(matrix[i][j]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            a = round(matrix[i][j] / div, 2)
            new_matrix[i].append(a)
    return new_matrix
