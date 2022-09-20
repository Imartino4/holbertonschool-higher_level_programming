#!/usr/bin/python3
""" No module imported """


class Square:
    """Defining the Square class"""
    def __init__(self, size=0):
        """
        Args:
        param1 (size): Square's size, must be an int >= 0

        """
        self.size = size

    def area(self):
        """
        Public method to return area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Property, retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Property setter, set a new size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
