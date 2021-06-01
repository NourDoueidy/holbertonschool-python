#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""

    def __inot__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, sixe, x, y, id)

    def __str__(self):
        """string representation of square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, id, x, y, width)
