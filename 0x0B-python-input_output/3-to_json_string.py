#!/usr/bin/python3

""" Thsi module contains a to_json_string()
"""
import json


def to_json_string(my_obj):
    """
    Returns the json representaion of an object
    """
    return json.dumps(my_obj)
