#!/usr/bin/python3
""" This module contains a function"""


def add_attribute(obj, attr_name, attr_value):
    """ A function that add an attribute to an object."""
    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
    if getattr(obj, attr_name) != attr_value:
        raise TypeError("can't add new attribute")
