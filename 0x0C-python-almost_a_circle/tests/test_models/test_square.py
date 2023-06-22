#!/usr/bin/python3
"""A test suite for models/square.py"""

import unittest

from models.square import Square
from io import StringIO
import sys
from unittest.mock import patch
import json


class TestSquare(unittest.TestCase):
    """Test suite for the Square class"""

    def setUp(self):
        """ set rectangle instances"""
        self.s1 = Square(1)
        self.s2 = Square(3)
        self.s3 = Square(4, 5, 2)
        self.s4 = Square(4, 2, 4)

    def test_size(self):
        """ test the value of width"""
        self.assertEqual(self.s1.size, 1)
        self.s1.size = 7
        self.assertEqual(self.s1.size, 7)

        with self.assertRaises(TypeError):
            r = Square("89")
        with self.assertRaises(ValueError):
            r = Square(0)
        with self.assertRaises(ValueError):
            r = Square(-2)

    def test_x(self):
        """ test the value of x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s3.x, 5)
        self.s4.x = 90
        self.assertEqual(self.s4.x, 90)

        with self.assertRaises(TypeError):
            self.s2.x = "4"

        with self.assertRaises(ValueError):
            self.s2.x = -1
        with self.assertRaises(TypeError):
            r = Square(89, "4")
        with self.assertRaises(ValueError):
            r = Square(89, -5)

    def test_y(self):
        """ Test The value of y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)
        with self.assertRaises(TypeError):
            r = Square(89, 9, "2")
        with self.assertRaises(ValueError):
            r = Square(89, 9, -9,)

    def test___str__(self):
        """ string representstion
        """
        self.assertTrue(hasattr(self.s3, "__str__"))
        r = "[{}] ({}) {:d}/{:d} - {:d}".format(self.s3.__class__.__name__,
                                                     self.s3.id, self.s3.x,
                                                     self.s3.y, self.s3.size)
        self.assertEqual(str(self.s3), r)

    def test_to_dictionary(self):
        """ test the to_dictionary()"""
        r = self.s4.to_dictionary()
        self.assertEqual(self.s4.to_dictionary(), r)
        self.assertTrue(hasattr(self.s3, "to_dictionary"))

    def test_update(self):
        """ test the update()"""
        self.assertTrue(hasattr(self.s4, "update"))
        self.s4.update(89, 1, 3, 4)
        self.assertEqual(self.s4.id, 89)
        self.assertEqual(self.s4.size, 1)
        self.assertEqual(self.s4.x, 3)
        self.assertEqual(self.s4.y, 4)
        r = self.s4.to_dictionary()
        self.s1.update(**r)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 4)

