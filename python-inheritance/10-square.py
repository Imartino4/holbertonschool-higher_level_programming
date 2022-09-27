#!/usr/bin/python3
""" This module create the Square class, a inheriths from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[{type(self).__name__}] {self.__size}/{self.__size}"
