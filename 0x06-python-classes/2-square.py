#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A square class with a private instance attribute"""


class Square:
    """ Square with size attribute"""
    def __init__(self, size=0):
        """ An instance of Square created with size atrribute
        Args:
            size (int): size of the square
        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")

