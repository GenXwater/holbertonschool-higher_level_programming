#!/usr/bin/env python3
"""
CountedIterator - Keeping Track of Iteration
"""


class CountedIterator:
    """
    This class allows you to count the number of itérables until there are no more items.
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count
