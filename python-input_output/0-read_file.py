#!/usr/bin/python3
""" Function on this module:
    red_file: reads a text file and print it to stdout
    """


def read_file(filename=""):
    """ receives the filename as a string and print the text to
        stdout"""

    with open(filename) as f:
        for line in f:
            print(line, en="")
    f.closed
