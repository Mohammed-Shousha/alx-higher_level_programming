#!/usr/bin/python3
"""
Contains the BaseGeometry class and Rectangle subclass
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Instantiation of the rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
