#!/usr/bin/python3
"""
This module has print_square implementation
"""


def print_square(size):
    """Prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    row = ["#" * size for _ in range(size)]
    print("\n".join(row))
