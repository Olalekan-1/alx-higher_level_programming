#!/usr/bin/python3

""" This module contains a function print_square()
"""


def print_square(size):
    """ This function prints square with '#'
    Args:
        size (int): The size of the square
    Raises:
        TypeError: if size is not int type
        ValueError: if size is < zero
        """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(int(size)):
        print('#' * size)

