#!/usr/bin/python3

""" This module contain a function defintion
"""


def is_kind_of_class(obj, a_class):
    """
    A function that check if an object is instance of
    a class.
    Returns:
        True if its an instance else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
