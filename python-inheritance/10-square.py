#!/usr/bin/python3
"""Module containing the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class defines a square.

    A square is a special case of a rectangle where all sides are equal.
    It inherits from the Rectangle class.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
                        Must be a positive integer.

        The size is validated and set as both the width and height
        of the square using the parent Rectangle class.
        """
        super().__init__(size, size)
        self.__size = size
