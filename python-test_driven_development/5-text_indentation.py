#!/usr/bin/python3
""" This module include text_indentation function,
    which modify a string """


def text_indentation(text):
    """This function receives a string and print a new line after a '.' '?' or ':'"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ':':
            if text[i] == " ":
                continue
        print(f"{text[i]}", end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")
