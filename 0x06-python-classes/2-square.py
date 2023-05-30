#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A square class with a private instance attribute"""


class Square:
    """ Square with size attribute"""
    def __init__(self, size=0):
        """ An instance of Square created with size atrribute
        Args:
            size (int): size of the square
        Raises:
            ValueError: If the size is less than 0.
            TypeError: If the size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
