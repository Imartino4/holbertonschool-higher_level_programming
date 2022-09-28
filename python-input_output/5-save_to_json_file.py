#!/usr/bin/python3
""" This module contains save_to_json_file function,
    which write an Object to a text file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """ Recevies an object and name of file,
    and write in it, the object in JSON representation"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
