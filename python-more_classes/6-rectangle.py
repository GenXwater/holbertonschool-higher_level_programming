#!/usr/bin/python3
"""
This module defines a class Rectangle with width and height management.
"""


class Rectangle:
    """
    This class defines a Rectangle with a private instance
    attributes: width and height.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        If either width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.
        If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rect = ""
        for j in range(self.height):
            rect += "#" * self.width
            if j < self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        for debugging purposes in the form of:
        <module_name.ClassName object at memory_address>
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
