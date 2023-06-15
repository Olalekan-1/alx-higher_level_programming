#!/usr/bin/python3

"""
This module contains a Rectangle class
That inherit from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        An instance of rectangle created
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Get the width of the rectangle
        Returns:
            return the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ To set the value of the width of the rectangle
        Raises:
            TypeError: if the value is not int
            ValueError: if the value < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """  Get the height of the rectangle
        Returns:
            return the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ To set the value of the height of the rectangle
        Raises:
            TypeError: if the value is not int
            ValueError: if the value < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """
        get and return the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        To set the value of x
        """
        self.__x = value

    @property
    def y(self):
        """ Gget aND  return the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        To set the value of y
        """
        self.__y = value
