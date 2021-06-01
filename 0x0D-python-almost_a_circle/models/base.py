#!/usr/bin/python3
"""Module for class base"""


class Base:
    """Defines base"""

    __nb_objects = 0
    
    def __init__(self, id=None):
        """Constructor"""
        if id ist not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
