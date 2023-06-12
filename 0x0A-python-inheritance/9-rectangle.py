#!/usr/bin/python3

"""
This module contains clases definition
"""


class BaseGeometry:
    """ A Base geometry class """

    def area(self):
        """ an area method
        Raises:
            Exception:...
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A function that assign name to a value
        and validate the value if it is an integer
        Raises:
            TypeError: if value is not int
            ValueError: if int <= 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ A sub class of BaseGeometry class"""

    def __init__(self, width, height):
        """ A intance Rectangel created
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ area of the rectangle
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ String reprsentation of Rectangle
        Returns:
            The string representation
        """
        r = f"[Rectangle] {self.__width} / {self.__height}"
        return r
