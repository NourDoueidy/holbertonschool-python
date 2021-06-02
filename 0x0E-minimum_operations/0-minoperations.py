#!/usr/bin/python3

def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly n H characters"""
    if n <= 1:
        return 0
    num, div, numOfOperations = n, 2, 0

    while num > 1:
        if num % div == 0:
            num = num / div
            numOfOperations = numOfOperations + div
        else:
            div += 1
    return numOfOperations
