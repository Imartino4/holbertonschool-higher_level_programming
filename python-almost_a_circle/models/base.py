#!/usr/bin/python3
""" Base class """

import json


class Base():
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This method recieves a list of dictionaries and returns the JSON
        string representation of that list """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method writes the JSON string representation of list_obj
            to a file """

        dict_list_objs = []
        for i in list_objs:
            dict_list_objs.append(i.to_dictionary())
        name = f"{cls.__name__}.json"
        with open(name, 'w') as f:
            f.write(Base.to_json_string(dict_list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ This method returns the list of the JSON string
        representation json_strin"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)
