#!/usr/bin/python3
"""
 Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a_class or its subclass,
    False otherwise.
    """
    return isinstance(obj, a_class)
