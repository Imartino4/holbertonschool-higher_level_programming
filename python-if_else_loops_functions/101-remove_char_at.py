#!/usr/bin/python3
def remove_char_at(str, n):
    # creates a copy of the string, removing the character at the position n
    print(f"{str[0:n]}{str[n + 1:]}")
