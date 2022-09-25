#!/usr/bin/python3
"""Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests"""

    def test_max_integer(self):
        self.assertEqual(max_integer([12, 0, -1, 18]), 18)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1.0, 2.1, 3.9, 0.7]), 3.9)
        self.assertEqual(max_integer([9]), 9)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

