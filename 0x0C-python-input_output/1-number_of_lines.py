#!/usr/bin/python3
"""Module for number of lines function"""


def number_of_lines(filename=""):
    """Function that counts number of lines"""
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())
