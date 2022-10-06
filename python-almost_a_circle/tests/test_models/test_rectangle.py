#!/usr/bin/python3
""" Unittest for Rectangle module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestRectangle(unittest.TestCase):
    """ Tests on Rectangle class """

    def Test_init(self):
        """Test on initialization"""
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3, 1)
        r3 = Rectangle(4, 4, 1, 1, 6)
        self.assertEqual(r1.id, 1)

    def Test_init_more_arguments(self):
        """ incorrect number of arguments """
        with self.assertRaise(TypeError):
            r1 = Rectangle(1)

if __name__ == '__main__':
    unittest.main()

