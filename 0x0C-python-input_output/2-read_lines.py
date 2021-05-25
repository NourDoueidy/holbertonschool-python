#!/usr/bin/python3
"""Module for reading lines function"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
                return

        count = 0
        for line in f:
            if count < nb_lines:
                print(line, end="")
            count += 1
