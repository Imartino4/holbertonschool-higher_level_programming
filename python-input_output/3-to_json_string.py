#!/usr/bin/python3
""" This module contains to_json_string function,
    which returns the JSON representation of an object
    """

import json


def to_json_string(my_obj):
    """Receives an object and return JSON representation"""
    return json.dumps(my_obj)
