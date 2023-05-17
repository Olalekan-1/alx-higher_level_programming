#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = set(my_list)
    add = 0
    for i in new:
        add += i
    return add
