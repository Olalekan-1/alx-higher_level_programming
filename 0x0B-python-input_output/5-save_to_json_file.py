#!/usr/bin/python3

"""
This module contains a save_to_json_file().
"""
import json


def save_to_json_file(my_obj, filename):
    """ Save the content of file in json format
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
