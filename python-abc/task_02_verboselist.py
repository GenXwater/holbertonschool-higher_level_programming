#!/usr/bin/env python3
"""
This module defines a built-in class list.
"""


class VerboseList(list):
    """
    A subclass of Python's built-in list that provides notifications
    when the list is modified.

    Methods:
    - append(item)
    - extend(iterable)
    - remove(item)
    - pop(index=-1)
    """

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extends the list with the elements from the iterable
        and prints a notification.
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the specified index
        and prints a notification.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
