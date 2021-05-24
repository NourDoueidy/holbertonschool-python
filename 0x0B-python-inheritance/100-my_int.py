#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """Defines MyInt class"""

    def __eq__(self, other):
        """override == operator inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """override != operator inverting it"""
        return int(self) == int(other)
