#!/usr/bin/python3
"""This module define a class Rectangle and gives width and height as
    private instance attribute
"""


class Rectangle:
    """
    Rectangle class
    Private attributes: width and height positives and integers
    """

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

# Public instance method area and perimeter
    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width != 0 and self.__height != 0:
            return self.__width * 2 + self.__height * 2
        return 0

    def __str__(self):
        rect = ""
        if self.__height > 0 and self.__width > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect = rect + "#"
                if i < self.__height - 1:
                    rect = rect + "\n"
        return(rect)
