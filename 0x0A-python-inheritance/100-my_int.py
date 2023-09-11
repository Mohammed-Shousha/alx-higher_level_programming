#!/usr/bin/python3
"""
Contains the MyInt class
"""


class MyInt(int):
    """Rebel version of an integer"""

    def __eq__(self, other):
        """Overrides the == operator with !="""
        return int(self) != other

    def __ne__(self, other):
        """Overrides the != operator with =="""
        return int(self) == other
