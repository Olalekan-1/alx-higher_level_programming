#!/usr/bin/python3
""" This module supplies a function, say_my_name(). for example,
>>> say_my_name("Olalekan", "Ahmed")
My name is Olalekan Ahmed
"""


def say_my_name(first_name, last_name=""):
    """ A function that print first and last names
    Args:
        first_name (string): The first name
        last_name (string): The last name
    Raises:
        TypeError: if last_name or first_name is not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
