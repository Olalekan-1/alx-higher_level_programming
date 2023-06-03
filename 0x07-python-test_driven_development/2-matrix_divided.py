#!/usr/bin/python3
""" This Module supplies one function, matrix_divided(). for example
>>> a = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(a, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """ This function divides the element of matrix by an int
    Args:
        matrix (list): The list of list to be divided
        div (int/ float): the divisor
        Raises:
            TypeError: for various condition of wrong type of argument
            ZeroDivisionError:if div is less than or equal to ZeroDivisionError
        Returns:
            The new list of all element divided by division
    """

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div <= 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                              "of integers/floats")
    for k in range(len(matrix)):
        if type(matrix[k]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    new = []
    for j in matrix:
        if len(j) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        row = []
        for i in j:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            row.append(round(i / div, 2))
        new.append(row)

    return new
