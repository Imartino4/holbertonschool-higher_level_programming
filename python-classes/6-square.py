#!/usr/bin/python3
""" No module imported """


class Square:
    """Defining the Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """ Create instance of Square class
        Args:
        param1 (size): Square's size, must be an int >= 0
        param2 (position): muste be a tuple with 2 positive integers

        """
        self.size = size
        self.position = position

    def area(self):
        """Public method to return area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Property, retrieve size"""
        return self.__size

    def position(self):
        """Property, retrieve position"""
        return self.position

    @size.setter
    def size(self, value):
        """Property setter, set a new size"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self, value):
        """Property setter, set position"""
        flag = 0
        if type(value) != tuple or len(value) != 2:
            flag = 1
        if type(value[0]) != int or type(value[1]) != int:
            flag = 1
        if value[0] <= 0 or value[1] <= 0:
            flag = 1
        if flag == 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def my_print(self):
        """ Public instance method that print a square with "#" """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print(f"{'#'}", end="")
                print()
