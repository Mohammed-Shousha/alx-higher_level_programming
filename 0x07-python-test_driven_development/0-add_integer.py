#!/usr/bin/python3
"""
This module has add_integer implementation
"""


def add_integer(a, b=98):
    """Returns the addition of a and b"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
