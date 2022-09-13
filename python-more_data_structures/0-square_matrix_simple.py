#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = len(matrix)
    n = len(matrix[0])
    square_matrix = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            square_matrix[i][j] = matrix[i][j] ** 2
    return square_matrix
