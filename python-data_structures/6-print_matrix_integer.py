#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i in n:
            print("{:d}".format(i), end="")
            if i != n:
                print(" ", end="")
        print()
