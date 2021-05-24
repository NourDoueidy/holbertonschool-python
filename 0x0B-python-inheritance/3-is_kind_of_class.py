#!/usr/bin/python3
"""Module for is kind of class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if:
            object is instance of class
            or object is an instance of class that inherited from class
    """
    return isinstance(obj, a_class)
