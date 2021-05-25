#!/usr/bin/python3
"""Module for json serialization"""


def class_to_json(obj):
    """Returns the dictionary representation with simple data structure"""
    return obj.__dict__
