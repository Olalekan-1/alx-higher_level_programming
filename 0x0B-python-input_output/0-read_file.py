#!/usr/bin/python3

""" This module contains a read_file()"""


def read_file(filename=""):
    """ Reads and prints the context of a file to the std. out
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for lines in f:
            print(lines, end='')
