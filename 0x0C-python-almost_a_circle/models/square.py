#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """init the square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, n_size):
        """setter for size"""
        self.width = n_size
        self.height = n_size

    def __str__(self):
        """return the string representation of the square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """updates the square instance arguments"""
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
