#!/usr/bin/python3

""" This module contains a load_from_json_file().
"""
import json


def load_from_json_file(filename):
    """ craete python object fron json filename
    """
    with open(filename, 'r', encoding='utf-8') as file:
        obj = json.load(file)
        return obj
