#!/usr/bin/python3
"""Base class"""
import json
import csv
from turtle import Turtle, Screen, exitonclick


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the CSV representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of classes from a file of csv strings"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws Rectangles and Squares using the turtle module."""
        WIDTH, HEIGHT = 360, 360

        screen = Screen()
        screen.setup(WIDTH + 4, HEIGHT + 8)
        screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)

        trt = Turtle()
        trt.screen.bgcolor("#000")
        trt.pensize(3)
        trt.shape("turtle")

        trt.hideturtle()
        trt.color("#fff")
        for rect in list_rectangles:
            trt.up()
            trt.goto(rect.x, rect.y)
            trt.down()
            for _ in range(2):
                trt.forward(rect.width)
                trt.left(90)
                trt.forward(rect.height)
                trt.left(90)

        trt.color("#41f0ed")
        for sq in list_squares:
            trt.up()
            trt.goto(sq.x, sq.y)
            trt.down()
            for _ in range(2):
                trt.forward(sq.width)
                trt.left(90)
                trt.forward(sq.height)
                trt.left(90)

        exitonclick()
