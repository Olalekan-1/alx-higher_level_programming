#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A square class with a private instance attribute"""


class Square:
    """ Square with size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """ An instance of Square created with size atrribute
        Args:
            size (int): size of the square
            position (tuple): cordinate position of the square
        Raises:
            ValueError: If the size is less than 0.
            TypeError: If the size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = None

    def area(self):
        """ Define and return the area of the square
        Returns:
            The area of the Square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ get the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.
        Args:
            value (int): value set to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ print square with # using the size value"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) and num > 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value * ' '
