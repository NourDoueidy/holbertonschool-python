#!/usr/bin/python3
"""Module for calss Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of a square"""
        return "[{}] (<{}>) <{}>/<{}> - <{}>".format(type(self).__name__, self.id, self.x, self.y, self.width)

