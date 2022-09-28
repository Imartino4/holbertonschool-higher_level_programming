#!/usr/bin/python3
"""This module contain from_json_string function,
    which returns an object represented by a JSON string
    """


import json


def from_json_string(my_str):
    """Recevies a string a return the object represented by
    JSON string"""
    return json.loads(my_str)
