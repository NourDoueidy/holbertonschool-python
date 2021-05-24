#!/usr/bin/python3
"""Module of attribute adding function"""

def add_new_attr(obj, att, value):
    """Adds new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
