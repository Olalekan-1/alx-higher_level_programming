#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeros if they are smaller than 2
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Extract first two elements from each tuple and perform addition
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
