#!/usr/bin/python3

""" This module contains a Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """ An instance of student created """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dic. rep. of attribute."""
        return self.__dict__
