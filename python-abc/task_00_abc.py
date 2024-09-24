#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses"""
        pass


class Dog(Animal):
    """Class representing a dog, inheriting from the Animal class."""

    def sound(self):
        """Returns the sound dog"""
        return "Bark"


class Cat(Animal):
    """Class representing a cat"""

    def sound(self):
        """Returns the sound cat"""
        return "Meow"
