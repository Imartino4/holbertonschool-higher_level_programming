#!/usr/bin/python3
""" Square Class """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Implementation of square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ Assign width and height with same value
            Use te same value validation as Rectangle"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Method to update a Square instance
            args (id, size, x, y)
            kwargs with key as attributes"""

        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            if kwargs:
                for k, v in kwargs.items():
                    setattr(self, k, v)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
