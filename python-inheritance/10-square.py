#!/usr/bin/python3
"""Module containing the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square's sides
        """
        super().__init__(size, size)
        self.__size = size
