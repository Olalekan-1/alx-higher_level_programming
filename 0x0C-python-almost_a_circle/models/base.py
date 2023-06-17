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

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_data)

    @classmethod
    def create(cls, **dictionary):
        """ return the set attribute
        of class instance
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Invalid class type")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """ laod from json file and return the list
        of all insatance with their attribute
        """
        filename = cls.__name__ + ".json"
        new = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                read = file.read()
        except FileNotFoundError:
            return new
        my_list = cls.from_json_string(read)
        for item in my_list:
            dict_rep = cls.create(**item)
            new.append(dict_rep)

        return new
