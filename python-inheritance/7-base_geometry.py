#!/usr/bin/python3
"""
A class named BaseGeometry.
"""


class BaseGeometry:
    """
    A base geometry class with area calculation and integer validation.
    """
    def area(self):
        """
        Calculates the area.
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        
        Args:
            name (str): The name of the value.
            value: The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
