#!/usr/bin/python3
"""Module to test City class."""
import unittest
from models.city import City


class TestState(unittest.TestCase):
    """Tests State class."""

    def test_type(self):
        """Makes sure attribute types are as expected."""
        my_model = City()
        self.assertTrue(type(my_model.name) is str)
        self.assertTrue(type(my_model.state_id) is str)
