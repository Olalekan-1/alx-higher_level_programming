#!/usr/bin/python3

""" This module contain a function defintion
"""


def inherits_from(obj, a_class):
    """
    A function that check if an object is subclass of
    a class.
    Returns:
        True if its an instance else False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
