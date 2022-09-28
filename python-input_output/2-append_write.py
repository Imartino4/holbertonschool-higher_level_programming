#!/usr/bin/python3
"""This module contain append_write function,
    which append a string to the end"""


def append_write(filename="", text=""):
    """Receives a text and the filename, and append the text at
    the end of the file"""
    with open(filename, 'a') as f:
        return f.write(text)
