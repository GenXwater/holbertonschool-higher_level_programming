#!/usr/bin/env python3


class Fish:
    """
    This class define a fish
    """
    def swim(self):
        print("The fish is swimming.")

    def habitat(self):
        print("The fish lives in water.")

class Bird:
    """
    This class define a bird
    """
    def fly(self):
        print("The bird is flying.")

    def habitat(self):
        print("The bird lives in the sky.")

class FlyingFish(Fish, Bird):
    """
    This class inherits two classes.
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
