#!/usr/bin/python3
def complex_delete(my_dict, value):
    keys_to_delete = []

    for key, val in my_dict.items():
        if val == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        my_dict.pop(key)

    return my_dict
