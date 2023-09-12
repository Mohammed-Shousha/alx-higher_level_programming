#!/usr/bin/python3
"""Contains save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """Converts `my_obj` python object into a json string and
    store it in `filename` file"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
