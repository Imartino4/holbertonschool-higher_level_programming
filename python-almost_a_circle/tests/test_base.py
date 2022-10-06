#!/usr/bin/python3
""" Unittest """

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestBase(unittest.TestCase):
    """Test on Base class"""

    def test_init(self):
        """ Test on initialization of Base, assuming that argument given
        are int"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base(None)
        b3 = Base(6)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 6)
        self.assertNotEqual(b3.id, 3)

    def test_wrong_init(self):
        """More than one argument when initalize a Base instance"""
        with self.assertRaises(TypeError):
            b4 = Base(5, 5)


class JsonTest(unittest.TestCase):
    """ Test on json methods """

    def test_to_json(self):
        """ Test on to_json_string method """
        r1_dict = {'x': 1, 'y': 1, 'id': 1, 'width': 6, 'height': 8}
        r2_dict = {'x': 0, 'y': 0, 'id': 2, 'width': 3, 'height': 3}
        json_dictionary = Base.to_json_string([r1_dict, r2_dict])
        reverse = json.loads(json_dictionary)
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(reverse, [r1_dict, r2_dict])

    def test_to_json_empty(self):
        """ Test an empty list on to_json_string method"""
        json_dict = Base.to_json_string([])
        self.assertEqual(type(json_dict), str)
        self.assertEqual(json_dict, "[]")

    def test_from_json_string(self):
        """ Test on from_json_string method"""
        s1 = Square(2, 4, 4, 1)
        s2 = Square (7, 0, 0, 2)
        s1_dict = s1.to_dictionary()
        s2_dict = s2.to_dictionary()
        json_string_dict = Base.to_json_string([s1_dict, s2_dict])
        json_list_dict = Base.from_json_string(json_string_dict)
        self.assertEqual(type(json_list_dict), list)
        self.assertEqual(type(json_list_dict[0]), dict)
    

if __name__ == "__main__":
    unittest.main()
