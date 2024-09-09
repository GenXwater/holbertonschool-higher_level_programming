#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n in matrix:
            for i in range(len(n)):
                print("{:d}".format(n[i]), end="")
                if i != len(n):
                    print(" ", end="")
            print()
