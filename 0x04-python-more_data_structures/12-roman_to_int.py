#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    result = 0 
    x = 0
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in reversed(roman_string):
        x = roman_dic[i]
        result = += x if result < x * 5 else -x
    return result
