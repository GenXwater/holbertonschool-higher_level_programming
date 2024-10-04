#!/usr/bin/python3
"""
Module for returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Args:
    my_obj: The object to be converted to JSON.

    Returns:
    str: A string containing the JSON representation of the object.
    """
    return json.dumps(my_obj)
