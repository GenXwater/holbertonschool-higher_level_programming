#!/usr/bin/python3
"""
Exact same object
"""


def is_same_class(obj, a_class):
    """True if the objet is exactly an instace of the specified class"""
    return type(obj) is a_class
