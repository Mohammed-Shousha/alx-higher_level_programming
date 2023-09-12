#!/usr/bin/python3
"""Contains load_from_json_file function"""


def load_from_json_file(filename):
    """Loads python object from json string stored in `filename` file"""
    import json
    with open(filename) as f:
        return json.load(f)
