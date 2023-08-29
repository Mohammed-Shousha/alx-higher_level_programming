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
	should be an int greater than 0.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
