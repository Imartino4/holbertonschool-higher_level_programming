#!/usr/bin/python3
""" Unittest for Square module """


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import io
import contextlib


class TestSquare(unittest.TestCase):
    """ Tests on Square class """

    def test_init(self):
        """Test on initialization"""
        s1 = Square(2)
        s2 = Square(2, 3,)
        s3 = Square(4, 4, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s3.y, 1)

    def test_init_no_arguments(self):
        """ No arguments given """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_init_more_arguments(self):
        """ More than expected arguments"""
        with self.assertRaises(TypeError):
            s3 = Square(2, 3, 0, 1, 2)

    def test_init_not_int(self):
        """ arguments are not integers"""
        with self.assertRaises(TypeError):
            s1 = Square("5", 3)
        with self.assertRaises(TypeError):
            s1 = Square(5, [3])
        with self.assertRaises(TypeError):
            s1 = Square(1, 3, "4")

    def test_init_negative_numbers(self):
        with self.assertRaises(ValueError):
            s1 = Square(-1, 3)
        with self.assertRaises(ValueError):
            s1 = Square(0, 3)
        with self.assertRaises(ValueError):
            s1 = Square(1, 3, -1)

    def test_area(self):
        """Test on area method"""
        s1 = Square(2, 5, 0, 1)
        self.assertEqual(s1.area(), 4)

    def test_str(self):
        """ Test __str__ method"""
        # Reset counter ob instances
        Base._Base__nb_objects = 0
        s2 = Square(4, 2, 0, 0)
        self.assertEqual(str(s2), "[Square] (1) 2/0 - 4")
    
    def test_display(self):
        """Test display method, import io and contextlib to test 
        stdout prints"""
        s3 = Square(2, 0, 0, 1)
        s4 = Square(2, 2, 2, 2)
        s5 = Square(2, 2, 0, 3)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            s3.display()
        self.assertEqual(buf.getvalue(), "##\n##\n")
        buf2 = io.StringIO()
        with contextlib.redirect_stdout(buf2):
            s4.display()
        self.assertEqual(buf2.getvalue(), "\n\n  ##\n  ##\n")
        buf3 = io.StringIO()
        with contextlib.redirect_stdout(buf3):
            s5.display()
        self.assertEqual(buf3.getvalue(), "  ##\n  ##\n")

    def teste_to_dictionary(self):
        """Test on to_dictionary method"""
        s1 = Square(2, 0, 0, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'x': 0, 'y': 0, 'size': 2, 'id': 1})

    def test_update(self):
        """Test on update method"""
        s1 = Square(10, 1, 1, 5)
        # change size wit *kwargs)
        s1.update(5, 3, 1, 1)
        self.assertEqual(s1.height, 3)
        # change x with **kwargs
        s1.update(x=9)
        self.assertEqual(s1.x, 9)

    def test_create(self):
        """Test on create method"""
        kwargs3 = {'id': 5, 'size': 16}
        kwargs4 = {'id': 5, 'size': 16, 'x': 2}
        kwargs5 = {'id': 5, 'size': 16, 'x': 2, 'y': 1}
        s3 = Square.create(**kwargs3)
        s4 = Square.create(**kwargs4)
        s5 = Square.create(**kwargs5)
        self.assertEqual(s3.size, 16)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s5.y, 1)

    def test_save_to_file(self):
        """Test on save to file method"""
        s1 = Square(5, 2, 2, 1)
        s2 = Square(6, 1, 1, 2)
        s1_d = s1.to_dictionary()
        s2_d = s2.to_dictionary()
        list_objects = [s1, s2]
        list_json = [s1_d, s2_d]
        Square.save_to_file(list_objects)
        # Now we check if the file contains the json string representation
        with open("Square.json", "r") as file:
            self.assertEqual(json.dumps(list_json), file.read())


        

if __name__ == '__main__':
    unittest.main()

