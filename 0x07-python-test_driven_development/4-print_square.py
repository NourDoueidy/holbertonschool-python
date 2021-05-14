#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Print a square with # character.
    Args:
        size (int): the size length of the square
    Raises:
        TypeError: if size is not an int
        ValueError: if size < 0
        TypeError: if size is a float or size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
