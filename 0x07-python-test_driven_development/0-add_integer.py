#!/usr/bin/python3
"""
This module is supply one function, add_integer(). for example,

>>> add_integer(7, 5)
12
"""


def add_integer(a, b=98):
    """ Function to add the value of two integer
    Args:
        a (int/ float): The first integer to add
        b (int/ flloat): The second number to add
    Returns:
        The addition of the 'a' and 'b' and must be int
    Raises:
        TypeError: if type 'a' and 'b' is not int or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
