#!/usr/bin/python3
"""
This module defines a class Square with size management.
"""


class Square:
    """
    This class defines a square with a private instance attribute: size.
    """

    def __init__(self, size=0):
        self.size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
