#!/usr/bin/python3
"""A test suite for models/rectangle.py"""

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle class"""

    def setUp(self):
        """ set rectangle instances"""
        self.r1 = Rectangle(1, 2)
        self.r2 = Rectangle(3, 4)
        self.r3 = Rectangle(4, 5, 2, 1)
        self.r4 = Rectangle(7, 6, 7)

    def test_width(self):
        """ test the value of width"""
        self.assertEqual(self.r1.width, 1)
        self.r1.width = 7
        self.assertEqual(self.r1.width, 7)

        with self.assertRaises(TypeError):
            r = Rectangle("89", 9)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 7)
        with self.assertRaises(ValueError):
            r =Rectangle(-2, 7)

    def test_height(self):
        """ test the value of height"""
        self.assertEqual(self.r1.height, 2)
        self.r1.height = 90
        self.assertEqual(self.r1.height, 90)
        with self.assertRaises(TypeError):
            r = Rectangle(89, "9")
        with self.assertRaises(ValueError):
            r = Rectangle(7, 0)
        with self.assertRaises(ValueError):
            r =Rectangle(7, -7)

    def test_x(self):
        """ test the value of x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)
        self.r4.x = 90
        self.assertEqual(self.r4.x, 90)

        with self.assertRaises(TypeError):
            self.r2.x = "4"

        with self.assertRaises(ValueError):
            self.r2.x = -1
        with self.assertRaises(TypeError):
            r = Rectangle(89, 9, "4")
        with self.assertRaises(ValueError):
            r = Rectangle(89, 9, -5)

    def test_y(self):
        """ Test The value of y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 1)
        with self.assertRaises(TypeError):
             r = Rectangle(89, 9, 9, "2")
        with self.assertRaises(ValueError):
             r = Rectangle(89, 9, 9, -9,)

    def test_area(self):
        """
        test area
        """
        self.assertEqual(self.r2.area(), 12)
        self.assertTrue(hasattr(self.r3, "area"))

    def test___str__(self):
        """ string representstion
        """
        self.assertTrue(hasattr(self.r3, "__str__"))
        r = "[{}] ({}) {:d}/{:d} - {:d}/{:d}".format(self.r3.__class__.__name__,
                                                     self.r3.id, self.r3.x,
                                                     self.r3.y, self.r3.width,
                                                     self.r3.height)
        self.assertEqual(str(self.r3), r)

    def test_display(self):
        """ Test display"""
        rec = "###\n###\n###\n###\n"
        buffer = StringIO()
        with patch("sys.stdout", buffer):
            self.r2.display()
        actual_value = buffer.getvalue()
        self.assertEqual(actual_value, rec)

        """r = Rectangle(4, 2, 2)
        rt = "  ####\n  ####\n"
        fake = StringIO
        with patch("sys.stdout", fake):
            r.display()
        real = fake.getvalue()
        self.assertEqual(real, rt)
        """

        rect = Rectangle(3, 2, 2, 2)
        rep = "\n\n  ###\n  ###\n"
        temp = StringIO()
        with patch("sys.stdout", temp):
            rect.display()
        value = temp.getvalue()
        self.assertEqual(value, rep)


