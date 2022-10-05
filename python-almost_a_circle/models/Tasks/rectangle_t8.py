#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for rectangle"""
        # Private attributes with setter and getter
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        # Use init method of Base for id
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = self.check_x(value)

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ method to calculate area """
        return self.__height * self.__width

    def display(self):
        """ public method to print rectangle in stdout with '#' """
        print(self.__y * '\n', end="")
        for i in range(self.__height):
            print(self.__x * ' ', end="")
            for i in range(self.__width):
                print ('#', end="")
            print()
    
    def __str__(self):
        """" __stt__ customized """
        return('[Rectangle] ' + '(' + str(self.id) + ') ' + str(self.x) + '/' + str(self.y) + ' - ' + str(self.width) + '/' + str(self.height))

    def update(self, *args):
        if len(args) == 1:
            super().__init__(args[0])
        if len(args) == 2:
            super().__init__(args[0])
            self.__width = args[1]
        if len(args) == 3:
            super().__init__(args[0])
            self.__width = args[1]
            self.__height = args[2]
        if len(args) == 4:
            super().__init__(args[0])
            self.__width = args[1]
            self.__heiht = args[2]
            self.__x = args[3]
        if len(args) == 5:
            super().__init__(args[0])
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
