#!/usr/bin/python3
""" This module contain write_file function,
which write a string to a text file"""


def write_file(filename="", text=""):
    """Receives filename and a text to write,
        return number of characters written"""
    with open(filename, 'w') as f:
        return f.write(text)
