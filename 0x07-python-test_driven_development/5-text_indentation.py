#!/usr/bin/python3
"""
This module has text_indentation implementation
"""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = False
    for i in text:
        if not flag and i == ' ':
            continue
        elif not flag and i != ' ':
            flag = True

        if flag and i in ['.', '?', ':']:
            print(i)
            print()
            flag = False
        elif flag:
            print(i, end="")
