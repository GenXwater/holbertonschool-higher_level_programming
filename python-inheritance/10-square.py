#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (9-base_geometry.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Initializes a Rectangle object
        Args:
            width: integer
            height: integer
        """
        super().__init__(size, size)
        self.__size = size
