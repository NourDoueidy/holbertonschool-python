#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    n_list = []
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("divided by 0")
        except IndexError:
            print("out of range")
        finally:
            n_list.append(res)
            i += 1
    return n_list
