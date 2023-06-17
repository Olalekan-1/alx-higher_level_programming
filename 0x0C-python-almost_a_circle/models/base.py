#!/usr/bin/python3

""" This module contains aBase class
"""
import json


class Base:
    """
    A base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ An instance of base class created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To represent in json format"""
        if list_dictionaries is None or list_dictionaries == []:
            return list()
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Return the object of json_string"""
        if not json_string or json_string == '':
            return list()
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json strings to json file"""
        new = []
        filename = cls.__name__ + ".json"
        for item in list_objs:
            rep = item.to_dictionary()
            new.append(rep)

        json_data = cls.to_json_string(new)

        with open(filename, 'w') as file:
            file.write(json_data)
