#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy
    for i in new_dic.keys():
        new_dic[i] = new_dic[i] * 2
    return new_dic
