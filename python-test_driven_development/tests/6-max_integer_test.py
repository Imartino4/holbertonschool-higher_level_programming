#!/usr/bin/python3
"""Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests"""

    def test_max_integer(self):
        self.assertEqual(max_integer([10, 5, 19, 8]), 19)

    def test_max_float(self):
        self.assertEqual(max_integer([-1.5, 4.6, 3.3, 8.7]), 8.7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_same_numbers(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_one_number(self)
        self.assertEqual(max_integer([0]), 0)
