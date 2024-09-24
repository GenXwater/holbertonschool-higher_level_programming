#!/usr/bin/python3
"""
An empty class named BaseGeometry.
"""


class BaseGeometry:
    """
    geometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
