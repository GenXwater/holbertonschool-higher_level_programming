#!/usr/bin/python3
"""
Learn JSON
"""


import json


def load_from_json_file(filename):
    """
    Args:
    filename (str): The name of the JSON file to read from
    Return:
    object: A Python object created from the JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
