#/usr/bin/python3
"""Module for search and append"""

def append_after(filename="", search_string="", new_string=""):
    text = ""
    with open(filename) as f:
        for i in f:
            text += i
            if search_string in i:
                text += new_string    
    with open(filename, "w") as g:
         g.write(text)
