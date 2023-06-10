#!/usr/bin/python3

""" This module contain a function defintion
"""


def is_same_class(obj, a_class):
    """
    A function that check if an object is instance of
    a class.
    Returns:
        True if its an instance else False
    """
    return type(obj) is a_class
