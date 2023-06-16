#!/usr/bin/python3

"""
This module contains a Square class,
it inherit from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A rectangle class that inherit from
    rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ An instance of square created"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square"""
        s = "[{}] ({}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width)
        return s

    @property
    def size(self):
        """ get and return the size of the
        of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the square class
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dict. rep. of the attribute
        """
        result = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return result
