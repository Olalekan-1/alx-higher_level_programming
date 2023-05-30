#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A square class with a private instance attribute"""


class Square:
    """ Square with size attribute"""
    def __init__(self, size):
        """ An instance of Square created with size atrribute
        Args:
            size (int): size of the square
        """
        self._size = size
