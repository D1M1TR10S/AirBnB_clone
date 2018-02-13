#!/usr/bin/python3
"""Module to test Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests Amenity class."""

    def test_type(self):
        """Makes sure attribute types are as expected."""
        my_model = Amenity()
        self.assertTrue(type(my_model.name) is str)
