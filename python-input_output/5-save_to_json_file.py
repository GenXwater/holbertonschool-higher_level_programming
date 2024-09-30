#!/usr/bin/python3
"""
Module for load the JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Args:
    my_obj: The Python object to be saved as JSON.
    filename (str): The name of the file to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
