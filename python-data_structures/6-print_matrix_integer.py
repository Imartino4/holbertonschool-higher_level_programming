#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if (j < n - 1):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")

        print("")
