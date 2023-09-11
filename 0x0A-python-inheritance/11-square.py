#!/usr/bin/python3
"""
Contains the Rectangle class and Square subclass
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Instantiation of the square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Informal string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
