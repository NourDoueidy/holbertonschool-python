#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    result = 0
    result1 = 0
    for i in len(my_list):
        result += (i[0] * i[1])
        result1 += i[1]
    return result / result1
