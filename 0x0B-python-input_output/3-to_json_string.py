#!/usr/bin/python3
"""Contains to_json_string function"""


def to_json_string(my_obj):
    """Converts `my_obj` python object into a json string"""
    import json
    return json.dumps(my_obj)
