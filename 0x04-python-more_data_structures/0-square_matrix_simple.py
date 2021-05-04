#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append(lambda x: x ** 2)
    return new_matrix
