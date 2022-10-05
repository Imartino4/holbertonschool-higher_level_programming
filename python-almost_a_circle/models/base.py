#!/usr/bin/python3
""" Base class """

import json
from os.path import exists


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
        if list_objs:
            for i in list_objs:
                dict_list_objs.append(i.to_dictionary())
        name = f"{cls.__name__}.json"
        with open(name, 'w') as f:
            f.write(Base.to_json_string(dict_list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ This method returns the list of the JSON string
        representation json_string"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_inst = cls(1)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of cls instances
            import os.path to exists function"""
        list_instances = []
        file_name = f"{cls.__name__}.json"
        if exists(file_name):
            with open(file_name, 'r') as f:
                instances = cls.from_json_string(f.read())
                for i in instances:
                    list_instances.append(cls.create(**i))
        return list_instances
