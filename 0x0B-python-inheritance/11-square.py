#!/usr/bin/python3
"""Module for class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a class square"""

    def __init__(self, size):
        """Constructor"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2

    def __str__(self):
        """print square description"""
        return "[Square]" + str(self.__size) + "/" + str(self.__size)
