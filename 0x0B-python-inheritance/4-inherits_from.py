#!/usr/bin/python3
"""Module for class inheritance"""


def inherits_from(obj, a_class):
    """Returns True if:
            obj is an instance of a class that inherited from a_class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
