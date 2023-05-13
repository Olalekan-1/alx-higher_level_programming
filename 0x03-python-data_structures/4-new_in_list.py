#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    new = my_list.copy()
    if idx < 0:
        return new
    elif idx > length - 1:
        return new
    else:
        new[idx] = element
        return new
