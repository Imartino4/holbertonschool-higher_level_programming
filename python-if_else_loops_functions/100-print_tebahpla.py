#!/usr/bin/python3
# This program print alphabet in reverse order alternating lowercase
# and upper case, with one prin, one loop and without import any module
for i in range(90, 64, -1):
    if i % 2 == 0:
        c = chr(i + 32)
    else:
        c = chr(i)
    print("{}".format(c), end="")
