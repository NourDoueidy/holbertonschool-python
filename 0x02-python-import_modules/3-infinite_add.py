#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) -1
    if n == 0:
        print("{}".format(n))
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])
    print(sum)
