#!/usr/bin/python3
""" This module include text_indentation function,
    which modify a string """


def text_indentation(text):
    """This function receives a string and
        print a new line after a '.' '?' or ':'
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = 1
    for i in text:
        if flag == 1 and i == " ":
            continue
        flag = 0
        print(f"{i}", end="")
        if i == ':' or i == '?' or i == '.':
            flag = 1
            print('\n')
