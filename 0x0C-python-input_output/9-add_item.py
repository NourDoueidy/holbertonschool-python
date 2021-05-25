#!/usr/bin/python3
"""Module for load, add, save json files"""

import json
import sys

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    python_list = load_from_json_file(filename)
except FileNotFoundError:
    python_list = []
finally:
    for i in sys.argv[1:]:
        python_list.append(i)
    save_to_json_file(python_list, filename)
