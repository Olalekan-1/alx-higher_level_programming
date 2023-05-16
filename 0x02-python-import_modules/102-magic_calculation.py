#!/usr/bin/python3

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def magic_calculation(a, b):
    from magic_calculation import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
