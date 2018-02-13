#!/usr/bin/python3
"""Module to test user class."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests User class."""

    def test_type(self):
        """Makes sure attribute types are as expected."""
        my_model = User()
        self.assertTrue(type(my_model.email) is str)
        self.assertTrue(type(my_model.password) is str)
        self.assertTrue(type(my_model.first_name) is str)
        self.assertTrue(type(my_model.last_name) is str)
