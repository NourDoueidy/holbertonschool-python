#!/usr/bin/python3
"""Module for JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a textfile, using JSON representation"""
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
