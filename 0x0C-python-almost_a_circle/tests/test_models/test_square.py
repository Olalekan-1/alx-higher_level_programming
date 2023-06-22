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
