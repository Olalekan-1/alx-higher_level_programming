#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = my_list.copy()
    for index, value in enumerate(new):
        if value == search:
            new[index] = replace
    return new
