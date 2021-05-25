#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """Defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(atts, list) and all(isinstance(ele, str) for ele in attrs):
            for i in attrs:
                if hasattr(self, i):
                    return i: getattr(self, i)
        return self.__dict__
