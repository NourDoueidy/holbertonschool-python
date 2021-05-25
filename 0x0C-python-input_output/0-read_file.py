#!/usr/bin/python3
"""Module for file reading function"""

def read_filename(filename=""):
    """function that reads a textfile and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") ad f:
        print(f.read(),end="")
