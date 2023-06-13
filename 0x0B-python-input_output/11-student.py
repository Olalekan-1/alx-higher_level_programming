#!/usr/bin/python3

""" This module contains a student class"""


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ An instance of class created"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dict repr of student attribut; filtered.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                filtered_dict[attr] = self.__dict__[attr]
        return filtered_dict

    def reload_from_json(self, json):
        """ change the key and value of the
        intitial attibute
        """
        for key, value in json.items():
            setattr(self, key, value)
