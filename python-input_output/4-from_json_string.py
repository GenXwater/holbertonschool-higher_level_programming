#!/usr/bin/python3
"""
Module for load the JSON file
"""


import json


def from_json_string(my_str):
    """
    Args:
    my_str: a json string to be converted to a python object.

    Returns:
    a python data structure
    """
    return json.loads(my_str)
