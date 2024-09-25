#!/usr/bin/env python3


from typing import SupportsIndex


class VerboseList(list):
    """
    A custom list class that provides verbose output for certain operations.
    This class extends the built-in list class with additional printing functionality.
    """

    def __init__(self, list):
        super().__init__(list)

    def append(self, obj):
        super().append(obj)
        print("Added [{}] to the list.".format(obj))

    def extend(self, obj):
        super().extend(obj)
        print("Extended the list with [{}] items.".format(obj))

    def remove(self, obj):
        super().remove(obj)
        print("Extended the list with [{}] items.".format(obj))

    def pop(self, obj=-1):
        obj = super().pop(obj)
        print("Popped [{}] from the list.".format(obj))
