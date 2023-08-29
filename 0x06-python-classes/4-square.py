#!/usr/bin/python3

"""
Module Square

Classes:
    Square - A square class
"""


class Square:
    """
    A square class

    Attributes:
        __size: private instance size

    Args:
        __size: the size of the square.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """get square size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set square size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
