#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {i: x*2 for i, x in a_dictionary.items()}
    return new
