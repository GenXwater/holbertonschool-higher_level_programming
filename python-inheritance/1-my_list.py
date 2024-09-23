#!/usr/bin/python3
"""
list object
"""


class MyList(list):
    """subclass of list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
