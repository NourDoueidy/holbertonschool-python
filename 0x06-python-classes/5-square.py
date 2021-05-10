#!/usr/bin/python3
"""define a square"""
def __init__(self, size=0):
    """initialize square
    """
    self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        return (self.size * self.size)

    def my_print(self):
        if self.__size == 0:
            print()
            return
    for i in range(0, self.__size):
        print("#", end="")
    print()       
    
