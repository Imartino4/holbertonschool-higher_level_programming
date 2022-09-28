#!/usr/bin/python3
""" This module contain load_from_json_file function,
which creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Receives a JSON file and returns the corresponding object"""
    with open(filename) as f:
        line = f.read()
        return json.loads(line)
