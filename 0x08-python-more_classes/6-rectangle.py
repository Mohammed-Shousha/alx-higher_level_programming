#!/usr/bin/python3
"""Module to define a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor of rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Printable representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """String representatino of  a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
