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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def update(self, *args, **kwargs):
        """ To update the rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ String reprsentation of Rectangle
        Returns:
            The string representation
        """
        r = "[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(self.__class__.__name__,
                                                     self.id, self.__x,
                                                     self.__y, self.__width,
                                                     self.__height)
        return r

    def area(self):
        """ Area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ display the the rectangle with`#`
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        """ Return the dict. rep. of the attributes
        """
        result = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return result
