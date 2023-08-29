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
        """Initialize a new square."""

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

        if type(size) is not int or type(size) is not float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
