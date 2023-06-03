#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided
try:
    '''matrix = [
        [2, 4, 6, 8],
        [10, 12, 14, 16]
    ]'''
    matrix = []
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)
