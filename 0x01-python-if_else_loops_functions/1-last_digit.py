#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
if number < 0:
    ldigit = -ldigit
print("Last digit of {:d} is {:d}".format(number, ldigit), end=" ")
if ldigit > 5:
    print("and is greater than 5")
elif ldigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
