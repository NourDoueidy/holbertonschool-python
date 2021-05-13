#!/usr/bin/python3
"""Defines a text indentation function."""

def text_indentation(text):
    """This function prints a text with 2 lines after ., ? and :
    Args:
        text(str): the text to print
    Raises TypeError if text is not a string
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join(
            [line.strip(" ")for line in text.split(char)])
    print(text, end="")
