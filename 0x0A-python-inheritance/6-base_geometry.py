#!/usr/bin/python3

"""
This module contain a Class definition
"""


class BaseGeometry:
    """ A Base geometry class """
    def __int__(self):
        """ an instance created """
        pass

    def area(self):
        """ an area method
        Raises:
            Exception:...
        """
        raise Exception("area() is not implemented")
