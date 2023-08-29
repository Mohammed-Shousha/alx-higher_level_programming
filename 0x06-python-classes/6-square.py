#!/usr/bin/python3

"""
Module Square

Classes:
    Square - A square class
"""


class Square:
    """
    A square class

    Args:
        size: the size of the square.
        position: the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get square position"""
        return self.__position

    @position.setter
    def position(self, position):
        """set square position"""
        if (not isinstance(position, tuple)
                or len(position) != 2
                or not all(isinstance(num, int) for num in position)
                or not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")
