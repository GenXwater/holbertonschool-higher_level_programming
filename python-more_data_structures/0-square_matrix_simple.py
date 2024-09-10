#!/usr/bin/python3

# simple version :
# return [[n ** 2 for n in row] for row in matrix]

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row = new_row + [n ** 2]
        new_matrix = new_matrix + [new_row]
    return new_matrix
