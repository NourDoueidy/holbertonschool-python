#!/usr/bin/python3
"""Module for class Square subclass of Rectangle"""
Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize a square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Calculates area"""
        return self.__size ** 2
