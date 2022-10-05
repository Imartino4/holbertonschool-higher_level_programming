#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for rectangle"""
        # Private attributes with setter and getter
        self.__width = self.check_width(width)
        self.__height = self.check_height(height)
        self.__x = self.check_x(x)
        self.__y = self.check_y(y)
        # Use init method of Base for id
        super().__init__(id)

    def check_width(self, width):
        """ Validate width """
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        else:
            return width

    def check_height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

    def check_x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

    def check_y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = self.check_width(value)

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = self.check_height(value)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = self.check_x(value)

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = self.check_y(value)

    def area(self):
        return self.__height * self.__width
