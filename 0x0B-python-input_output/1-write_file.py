#!/usr/bin/python3

""" This module contains a write_file()
"""


def write_file(filename="", text=""):
    """ create file if doesnt exit, write text into the file
    overit content if file already exist.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        file = f.write(text)
    return file
