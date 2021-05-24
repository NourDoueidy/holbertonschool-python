#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class inheriting from BaseGeometry"""
   
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """prints width and height of rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
