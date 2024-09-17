#!/usr/bin/python3

class Square:
    """
    This class defines a square with a private instance attribute: size.
    """
    
    def __init__(self, size=0, position=(0, 0)): #
        self.size = size
        self.position = position

    @property
    def position(self): #
        return self.__position
    
    @position.setter
    def position(self, value): #
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    @property
    def size(self): #
        return self.__size
    
    @size.setter
    def size(self, value): #
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self): #
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
