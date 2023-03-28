#!/usr/bin/python3
"""This module creates square class"""


class Square:
    """Class Square that defines a square.
    """
    def __init__(self, size=0):
        """Initialize the class
        Args:
            size (int): size of the square
        """
        if type(size).__name__ != "int":
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size).__name__ != "int":
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Print the square"""
        for i in range(self.__size):
            if i != 0:
                print()
            for j in range(self.__size):
                print("#", end="")
        print()
