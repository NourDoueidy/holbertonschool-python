#!/usr/bin/python3
"""rotate 2d matrix"""


def rotate_2d_matrix(matrix):
    """function that rotates matrix 90 degrees in-place"""
    matrix.reverse()
    for i in range len(matrix):
        for j in range (i):
            matrix [i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
