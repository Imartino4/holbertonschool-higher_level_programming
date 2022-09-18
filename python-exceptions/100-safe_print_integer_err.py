#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as mess:
        print("Exception: {}".format(mess), file = sys.stderr)
        return False

