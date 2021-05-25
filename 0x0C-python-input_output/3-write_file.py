#!/usr/bin/python3
"""Module for writing into a file"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the nb of characters"""
    with open(filename, "w", encoding="utf-8") as f:
         return f.write(text)
