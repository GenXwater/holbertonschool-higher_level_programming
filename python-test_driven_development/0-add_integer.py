#!/usr/bin/python3
"""Function that adds 2 integers."""

def add_integer(a, b=98):
    """
    a and b must be integers or floats

    Returns:
    sum of a and b

    Raises
    TypeError if a and b is not integer or float 
    """

    if not isinstance(a (int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
