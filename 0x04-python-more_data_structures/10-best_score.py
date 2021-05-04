#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = None
    max_value = 0
    for a, b in a_dictionary.items():
        if a > max_value:
            max_value = a
            max_key = b
    return max_key
