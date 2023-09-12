#!/usr/bin/python3
""" Script to add all arguments to a Python list and save them to a file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Adds all arguments to a Python list and save them to a file."""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
        items.extend(sys.argv[1:])
    except FileNotFoundError:
        items = []

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()
