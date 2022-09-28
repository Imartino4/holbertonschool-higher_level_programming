#!/usr/bin/python3
"""This module contains class_to_json function,
which returns the dict description with simple data structure
for JSON serialization of an object"""


def class_to_json(obj):
    """receives an object and return the dictionary description"""
    return obj.__dict__
