#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
lastDigit = number % 10
print("Last digit of {} is {}".format(number, lastDigit))
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
elif 0 < lastDigit < 6:
    print("and is less than 6 and not 0")
    

    