#!/usr/bin/python3
"""
list object
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """Initialize objet"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
