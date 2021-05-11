#!/usr/bin/python3
"""Square module"""

class Square:
    """Define a square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initiate a square class.
        Args:
            size
            position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set size"""
        return self.__size
   
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0 :
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set position"""
        self.__position = position
    
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or value < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        if type(value[0]) 1= int and type(balue[1]) != int: 
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """return area"""
        return self.__size * self.__size
    
    def my_print(self):
        """print the square with the # character."""
        if self.__size = 0
        print("")
        return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
