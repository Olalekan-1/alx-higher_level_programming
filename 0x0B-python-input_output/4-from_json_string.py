#!/usr/bin/python3

""" This module contains a from_json_string()
"""
import json


def from_json_string(my_str):
    """
    Returns the python representaion of json.
    """
    return json.loads(my_str)
