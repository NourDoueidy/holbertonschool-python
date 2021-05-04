#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    max_key = None
    for a, b in a_dictionary.items():
        if b > max_value:
            max_value = b
            max_key = a
    return max_key
