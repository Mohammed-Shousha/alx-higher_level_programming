#!/usr/bin/python3
"""Contains append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Appends `new_string` after a line containing
    `search_string` in `filename`"""
    with open(filename, 'r+') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if search_string in line:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.writelines(lines);
