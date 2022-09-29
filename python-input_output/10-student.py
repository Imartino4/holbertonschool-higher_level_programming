#!/usr/bin/python3
"""This module create Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        aux_count = 0
        aux_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) == str:
                    aux_count += 1
            if aux_count == len(attrs):
                for i in attrs:
                    if i in self.__dict__:
                        aux_dict[i] = self.__dict__[i]
                return aux_dict
        return self.__dict__
