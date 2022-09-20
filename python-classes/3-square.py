#!/usr/bin/python3
""" No module imported """


class Square:
    """Defining the Square class"""
    def __init__(self, size=0):
        """
        Args:
        param1 (size): Square's size, must be an int >= 0

        Exceptions:
        TypeError when size is not an integer
        ValueError when size is less than 0

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
