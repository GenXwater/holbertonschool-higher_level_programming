#!/usr/bin/python3
"""Function that adds 2 integers."""


def add_integer(a, b=98):
    """
    Adds two numbers, ensuring they are integers.

    Args:
        a: The first number, must be an integer or a float.
        b: The second number, must be an integer or a float (default is 98).

    Returns:
        The sum of a and b as integers.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
