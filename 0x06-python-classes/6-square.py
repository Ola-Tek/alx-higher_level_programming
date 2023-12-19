#!/usr/bin/python3
"""Define a class sequence."""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size (int): The size of the new square
            position (int, int): The positioning of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the present size of the swuare"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be an >= 0")
        self.__size = value

    @property
    def position(self):
        """get the present positoonof the swuarr"""
        return (self.__position)

    @property.setter
    def position(self, value):
        if (not isinstance(value, turple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a turple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """print tge square with the #character"""
        if self.__size == 0:
            print("")
            return

    [print("") for i in range(0, self.__position[1])]
    for i in range(0, self.__size):
        [print(" ", end="") for j in range(0, self.__position[0])]
        [print("#", end="") for k in range(0, self.__size)]
        print("")
