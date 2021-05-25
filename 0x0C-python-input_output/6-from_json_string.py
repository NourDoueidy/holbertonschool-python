#!/usr/bin/python3
"""Module for json string"""

import json


def from_json_string(my_str):
    """Returns a python object represented by json string"""
    return json.loads(my_str)
