#!/usr/bin/python3
"""Module to test Review class."""
import unittest
from models.review import Review


class TestState(unittest.TestCase):
    """Tests State class."""

    def test_type(self):
        """Makes sure attribute types are as expected."""
        my_model = Review()
        self.assertTrue(type(my_model.place_id) is str)
        self.assertTrue(type(my_model.user_id) is str)
        self.assertTrue(type(my_model.text) is str)
