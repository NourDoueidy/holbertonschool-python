#!/usr/bin/python3
"""Module for file-reading function"""

import json


def load_from_jason_file(filename):
    """Create a python object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
