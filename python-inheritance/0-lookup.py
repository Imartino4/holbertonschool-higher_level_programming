#!/usr/bin/python3
""" This module contain lookup function
    lookup return a list of attributes and
    methods of an object
    """

def lookup(obj):
    """Receives an object and return a list of
    attributes and methods of it"""
    return dir(obj)
