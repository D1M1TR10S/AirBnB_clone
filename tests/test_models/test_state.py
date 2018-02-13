#!/usr/bin/python3
"""Module to test user class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests State class."""

    def test_type(self):
        """Makes sure attribute types are as expected."""
        my_model = State()
        self.assertTrue(type(my_model.name) is str)
