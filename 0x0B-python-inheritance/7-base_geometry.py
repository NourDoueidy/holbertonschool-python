#!/usr/bin/python3
"""Module for integer validator"""


class BaseGeometry:
    """Defines a class"""
    def area(self):
        """Function that calculates area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Function that validate integers"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
