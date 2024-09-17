#!/usr/bin/python3

class Square:
    """
    This class defines a square with a private instance attribute: size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Getter for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position. Validates that position is a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """
        Getter for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size. Validates that size is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' considering the position.
        If size is 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
