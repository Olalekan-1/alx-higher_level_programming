#!/usr/bin/python3
""" This module contains a class_to_json class"""


def class_to_json(obj):
    """
    class_to_json class"""
    result = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value
    return result
