#!/usr/bin/python3
"""Contains from_json_string function"""


def from_json_string(my_str):
    """Converts `my_str` json string into a python object"""
    import json
    return json.loads(my_str)
