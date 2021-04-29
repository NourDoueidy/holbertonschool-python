#!/usr/bin/python3
import sys

n = len(argv) - 1
if n == 0:
    print("0 arguments.")
elif n == 1:
    print("1 argument:")
else :
    print("{} arguments:".format(n))
while i <= n:
    print("{}: {}".format(i,argv[i]))
    i += 1
