#!/usr/bin/python3

"""
This module contains a  class
"""


class LockedClass:
    """ A locked class that  with no attribute an prevents
    dynamically craeting of instance
    """
    __slots__ = ["first_name"]

    def __int__(self, value):
        """
        instance can only be created with first_name atttribute
        Args:
            value of the attribute
        """
        self.first_name = value
