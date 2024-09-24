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

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        This method overrides the area method from the Rectangle class,
        although it produces the same result for a square.
        """
        return self.__size ** 2
