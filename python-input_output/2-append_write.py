#!/usr/bin/python3
"""
Module for writes a string to a text file (UTF8)
and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    Module for function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
