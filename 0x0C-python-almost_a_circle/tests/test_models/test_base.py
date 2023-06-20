#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import turtle


class Testbase(unittest.TestCase):
    """ TestCases to test the base instance
    """

    def setUp(self):
        """ The tests setUp"""
        self.poly1 = Base()
        self.poly2 = Base()
        self.poly3 = Base()
        self.poly4 = Base()

    def test_instance_id(self):
        """ Test the instance id"""
        self.assertEqual(self.poly1.id, 1)
        self.assertEqual(self.poly2.id, 2)
        self.assertEqual(self.poly3.id, 3)
        self.assertEqual(self.poly4.id, 4)
