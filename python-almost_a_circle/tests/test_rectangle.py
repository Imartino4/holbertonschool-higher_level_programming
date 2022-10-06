#!/usr/bin/python3
""" Unittest for Rectangle module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
import json
import io
import contextlib


class TestRectangle(unittest.TestCase):
    """ Tests on Rectangle class """

    def test_init(self):
        """Test on initialization"""
        r1 = Rectangle(2, 3)
        r2 = Rectangle(2, 3, 1)
        r3 = Rectangle(4, 4, 1, 1, 6)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r3.height, 4)

    def test_init_no_arguments(self):
        """ No arguments given """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_init_one_argument(self):
        """ Only one argument"""
        with self.assertRaises(TypeError):
            r2 = Rectangle(1)

    def test_init_more_arguments(self):
        """ More than expected arguments"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(2, 3, 0, 0, 2, 6)

    def test_init_not_int(self):
        """ arguments are not integers"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("5", 3)
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, [3])
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 3, "4")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 4, "7")

    def test_init_negative_numbers(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 3)
        with self.assertRaises(ValueError):
            r1 = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 3, -1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 4, -5)

    def test_area(self):
        """Test on area method"""
        r1 = Rectangle(2, 5, 0, 0 ,1)
        self.assertEqual(r1.area(), 10)

    def test_str(self):
        """ Test __str__ method"""
        r2 = Rectangle(4, 2, 0, 0, 2)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 4/2")
    
    def test_display(self):
        """Test display method, import io and contextlib to test 
        stdout prints"""
        r3 = Rectangle(3, 2, 0, 0, 1)
        r4 = Rectangle(3, 2, 2, 2, 2)
        r5 = Rectangle(3, 2, 2, 0, 3)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            r3.display()
        self.assertEqual(buf.getvalue(), "###\n###\n")
        buf2 = io.StringIO()
        with contextlib.redirect_stdout(buf2):
            r4.display()
        self.assertEqual(buf2.getvalue(), "\n\n  ###\n  ###\n")
        buf3 = io.StringIO()
        with contextlib.redirect_stdout(buf3):
            r5.display()
        self.assertEqual(buf3.getvalue(), "  ###\n  ###\n")

    def teste_to_dictionary(self):
        """Test on to_dictionary method"""
        r1 = Rectangle(2, 3, 0, 0, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 0, 'y': 0, 'height': 3, 'width': 2, 'id': 1})

    def test_update(self):
        """Test on update method"""
        r1 = Rectangle(10, 10, 1, 1, 5)
        # change width and height with *args)
        r1.update(5, 4, 3, 1, 1)
        self.assertEqual(r1.height, 3)
        # change x with **kwargs
        r1.update(x=9)
        self.assertEqual(r1.x, 9)
        

if __name__ == '__main__':
    unittest.main()

