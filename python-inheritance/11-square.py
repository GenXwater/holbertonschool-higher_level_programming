#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (9-base_geometry.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Initializes a square object
        Args:
            width: integer
            height: integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of a Rectangle object"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of a Rectangle object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
