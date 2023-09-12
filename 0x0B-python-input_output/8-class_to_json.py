#!/usr/bin/python3
"""Contains class_to_json function"""


def class_to_json(obj):
    """
    Returns the dictionary description of a
    class with simple data structure
    """
    return obj.__dict__
