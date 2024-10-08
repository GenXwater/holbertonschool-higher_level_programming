#!/usr/bin/python3
"""
Learn
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [0] * (i + 1)
        row[0] = 1
        row[i] = 1

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle += [row]

    return triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


print_triangle(pascal_triangle(6))