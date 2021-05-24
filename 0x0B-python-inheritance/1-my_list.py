#!/usr/bin/python3
"""Module for class inheritance"""


class Mylist(list):
    """Represents a list"""

    def print_sorted(self):
        """Prints the list sorted"""
        print(sorted(self))
