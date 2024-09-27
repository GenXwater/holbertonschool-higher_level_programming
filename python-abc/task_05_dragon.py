# task_05_dragon.py
"""
Define the SwimMixin with a swim method
"""


class SwimMixin:
    """
    Class SwimMixin
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
