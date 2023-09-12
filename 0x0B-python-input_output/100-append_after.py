#!/usr/bin/python3
"""Contains append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Appends `new_string` after a line containing
    `search_string` in `filename`"""
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
