#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(*args)
        return a
    except Exception as mess:
        print("Exception: {}".format(mess), file=sys.stderr)
        return None
