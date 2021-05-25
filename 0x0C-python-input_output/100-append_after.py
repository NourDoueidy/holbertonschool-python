#!/usr/bin/python3
"""Module for search and append"""

def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string"""
    text = ""
    with open(filename) as o:
        for line in o:
            text += line
            if search_string in line:
                text += new_string    
    with open(filename, "w") as p:
         p.write(text)
