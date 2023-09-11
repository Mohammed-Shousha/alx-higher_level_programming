#!/usr/bin/python3
"""Contains the add_attribute function."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
