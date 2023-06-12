#!/usr/bin/python3

"""
This module contain a Class definition
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

