#!/usr/bin/python3
"""Square module."""
class Square:
    """Defines a square.
    """
    pass
    def __init__(self, size=0)
        """Initialize a new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
