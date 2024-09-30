#!/usr/bin/python3
"""Module for read file"""


def read_file(filename=""):
    """
    read file with text in utf8
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
