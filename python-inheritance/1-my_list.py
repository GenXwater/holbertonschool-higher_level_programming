#!/usr/bin/python3
"""
list object
"""


class MyList(list):
    """
    that prints the list, but sorted
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
