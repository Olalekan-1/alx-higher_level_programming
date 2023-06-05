#!/usr/bin/python3

"""
This module contains a Rectagle class definition with its
associated methods.
"""


class Rectangle:
    """
    A definition of a rectangle class.
    """
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """ define a class methods
        Returns:
            The class instance of Rectangle
        """
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
        An instances of a for rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        Raises:
            TypeError: if type of height and width not int
            ValueError: if height  and width is less zero
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """  Get the height of the rectangle
        Returns:
            return the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ To set the value of the height of the rectangle
        Raises:
            TypeError: if the value is not int
            ValueError: if the value < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Get the width of the rectangle
        Returns:
            return the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ To set the value of the width of the rectangle
        Raises:
            TypeError: if the value is not int
            ValueError: if the value < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ define and return the area of the rectangle
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ defines and return the perimeter of the rectangle
        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    '''
    def __str__(self):
        """ represent the rectangle with char '#'
        Returns:
            the representation of the triangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += self.print_symbol * self.__width + "\n"
        return rect_str.rstrip("\n")
    '''

    def __str__(self):
        """ represent the rectangle with char 'print_symbol'
        Returns:
            the representation of the rectangle
        """
        rectangle_str = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(str(self.print_symbol))
            rectangle_str.append("".join(row))
        return "\n".join(rectangle_str)

    def __repr__(self):
        """ representation of the rectangle
        Returns:
            the representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Detroy/ delete an object instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ a staticmethod that return the biggest rectangle
        Args:
            rect_1 (Rectangle) : the first rectangle
            rect_2 (Rectangle) : the second rectangle
        Raises:
            TypeError: if rect_1 or rect_2 is not type of Rectangle
        Returns:
            The bigest rectangle
            """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
