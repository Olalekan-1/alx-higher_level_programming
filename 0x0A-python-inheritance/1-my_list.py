#!/usr/bin/python3
"""
This module contains a class that inherit from
inbuilt list object
"""


class MyList(list):
    """ MyList class; it inherit the properties of
    inbuilt list
    """
    def __init__(self):
        """ An instance of MYlist created"""
        super().__init__()

    def print_sorted(self):
        """ prints the element of the list in ascending order
        """
        print(sorted(self))
