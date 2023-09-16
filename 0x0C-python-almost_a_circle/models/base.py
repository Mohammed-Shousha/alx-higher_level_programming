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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(Base.to_json_string(
                    [i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries from json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from dictionary representation"""
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of classes instantiated from a json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dict = Base.from_json_string(file.read())
                return [cls.create(**cls_dict) for cls_dict in list_dict]
        except IOError:
            return []
