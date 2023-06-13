#!/usr/bin/python3

""" This module contains a append_after()"""


def append_after(filename="", search_string="", new_string=""):
    ''' Append a new_string if search_stringis found in a line
    '''
    with open(filename, 'r+', encoding='utf-8') as file:
        line = file.readlines()
        file.seek(0)
        for lin in line:
            file.write(lin)
            if search_string in lin:
                file.write(new_string)
        file.truncate()
