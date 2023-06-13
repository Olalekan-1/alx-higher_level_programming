#!/usr/bin/python3

""" This module contains a append_file()
"""


def append_write(filename="", text=""):
    """write text into the file
    append content if file already exist.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        file = f.write(text)
    return file
