#!/usr/bin/python3

""" printing the square of a  element of a
 2d matrix using list comprehension """


def square_matrix_simple(matrix=[]):
    new = [[x**2 for x in i] for i in matrix]
    return new
