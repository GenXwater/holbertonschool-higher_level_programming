#!/usr/bin/env python3
"""
This module defines a built-in class list.
"""


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
        length = len(self)
        super().extend(obj)
        obj_added = len(self) - length
        print("Extended the list with [{}] items.".format(obj_added))

    def remove(self, obj):
        if obj in self:
            print("Removed [{}] from the list.".format(obj))
            super().remove(obj)
        else:
            print("Item [{}] not found in the list.".format(obj))

    def pop(self, obj=-1):
        if self:
            item = self[obj]
            print("Popped [{}] from the list.".format(item))
            return super().pop(obj)
        else:
            raise IndexError("pop from empty list")
