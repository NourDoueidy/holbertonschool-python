#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates class"""
        if args:
            if len(args) >= 2:
                self.__size = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
                
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
