#!/usr/bin/python3


class Square:
    """ A square class with a private instance attribute """
    def __init__(self, size):
        """
        parameter
        _________
        size : int
            The size of the square
        """
        self._size = size

    def area(self):
        """ Define and return the area of the square """
        return self._size ** 2

    def perimeter(self):
        """ Define and return the perimeter of the square """
        return 4 * self._size
