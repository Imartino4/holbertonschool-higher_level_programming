#!/usr/bin/python3
def print_last_digit(number):
    n = number
    if (n < 0):
        n = n * -1
    n = n % 10
    print(f"{n}", end="")
    return n
