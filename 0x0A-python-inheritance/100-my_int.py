#!/usr/bin/python3

""" this module contains MyInt class
"""


class MyInt(int):
    """ MyInt class """
    def __eq__(self, other):
        """ '==' inverted"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ '!=" inverted"""
        return super().__eq__(other)
