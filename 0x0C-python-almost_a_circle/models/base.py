#!/usr/bin/python3
"""Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts `list_dictionaries` to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
