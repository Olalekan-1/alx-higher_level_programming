#!/usr/bin/python3
import math

""" Debuging and representing a Magic Class bytecode """


class MagicClass:
    """ A magic class and it asscociated methods and attributes"""
    def __init__(self, radius=0):
        """ A instance of the Magical Class created
        Args:
            radius (int/float) : The radius of the class
        Raises:
            TypeError: if radius is  not float or int
        """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ area of the magic Class
        Returns:
            The area of the magic class
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ The circumference of the magic Class
        Returns:
            The circumfernce
        """
        return 2 * math.pi * self.__radius
