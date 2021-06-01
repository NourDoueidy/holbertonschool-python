#!/usr/bin/python3
"""Module for class base"""
import json


class Base:
    """Defines a class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            if type(list_dictionaries) is not list:
                raise TypeError("list_dictionaries must be a list")
            jsoned = json.dumps(list_dictionaries)
            return jsoned
