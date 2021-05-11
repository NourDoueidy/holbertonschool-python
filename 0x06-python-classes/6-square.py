#!/usr/bin/python3
"""Square moule."""
class Square:
    """Define a square.
    """

    def __init__(self, size=0, position = (0, 0):
        """Initialize square
        Args:
            size(int): size of the square
            position(int, int): position of the square
        """
        self.size = size
        position.self = position
    
    @property
    def size(self):
        """Get/set the size of the square"""
        return self.__size
 
    @size.setter
    def size(self, size)
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
    
    def area(self):
        """return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0 :
        print()
        return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for i in range(0, self.__size):
                print("#", end="")
        print("")
