#!/usr/bin/python3

"""
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import turtle
from unittest.mock import patch


class Testbase(unittest.TestCase):
    """ TestCases to test the base instance
    """

    def setUp(self):
        """ The tests setUp"""
        self.poly1 = Base()
        self.poly2 = Base()
        self.poly3 = Base(8)
        self.poly4 = Base()

    def test_instance_id(self):
        """ Test the instance id"""
        self.assertEqual(self.poly1.id, 4)
        self.assertEqual(self.poly2.id, 5)
        self.assertEqual(self.poly3.id, 8)
        self.assertEqual(self.poly4.id, 6)

    def test_to_json_string(self):
        """ Test the to_json_string()."""
        self.assertEqual(self.poly1.to_json_string(None), '[]')
        self.assertEqual(self.poly2.to_json_string([]), '[]')
        self.assertEqual(self.poly3.to_json_string([{'id': 12}]),
                         '[{"id": 12}]')

    def test_from_json_string(self):
        """ Test the from_json_string():"""
        self.assertEqual(self.poly1.from_json_string(None), [])
        self.assertEqual(self.poly2.from_json_string("[]"), [])
        self.assertEqual(self.poly3.from_json_string('[{"id": 12}]'), [{'id': 12}])


if __name__ == '__main__':
    unittest.main()
