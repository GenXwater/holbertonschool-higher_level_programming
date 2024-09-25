#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class that represent a shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Class that represent a circle"""

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        """Get the radius of the circle"""
        return self.__radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def perimeter(self):
        return self.__radius * 2 * math.pi


class Rectangle(Shape):
    """Class that reprent a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
