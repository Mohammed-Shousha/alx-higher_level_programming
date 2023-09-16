#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class representation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init the class and set it"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
