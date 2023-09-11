#!/usr/bin/python3
"""
Contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """Returns True if obj isexactly an instance of a_class, otherwise False"""

    return type(obj) == a_class
