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
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -7)
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 6)

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

    def test_create(self):
        """Test on create method"""
        kwargs3 = {'id': 5, 'width': 16, 'height': 8}
        kwargs4 = {'id': 5, 'width': 16, 'height': 8, 'x': 2}
        kwargs5 = {'id': 5, 'width': 16, 'height': 8, 'x': 2, 'y': 1}
        r3 = Rectangle.create(**kwargs3)
        r4 = Rectangle.create(**kwargs4)
        r5 = Rectangle.create(**kwargs5)
        self.assertEqual(r3.height, 8)
        self.assertEqual(r4.x, 2)
        self.assertEqual(r5.y, 1)

    def test_save_to_file(self):
        """Test on save to file method"""
        r1 = Rectangle(5, 4, 2, 2, 1)
        r2 = Rectangle(6, 6, 1, 1, 2)
        r1_d = r1.to_dictionary()
        r2_d = r2.to_dictionary()
        list_objects = [r1, r2]
        list_json = [r1_d, r2_d]
        Rectangle.save_to_file(list_objects)
        # Now we check if the file contains the json string representation
        with open("Rectangle.json", "r") as file:
            self.assertEqual(json.dumps(list_json), file.read())

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

if __name__ == '__main__':
    unittest.main()

