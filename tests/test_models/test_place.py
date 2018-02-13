#!/usr/bin/python3
"""Module to test place class."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests Place class."""

    def test_type(self):
        """Makes sure attribute types are as expected."""
        my_model = Place()
        self.assertTrue(type(my_model.name) is str)
        self.assertTrue(type(my_model.city_id) is str)
        self.assertTrue(type(my_model.user_id) is str)
        self.assertTrue(type(my_model.description) is str)
        self.assertTrue(type(my_model.number_rooms) is int)
        self.assertTrue(type(my_model.number_bathrooms) is int)
        self.assertTrue(type(my_model.max_guest) is int)
        self.assertTrue(type(my_model.price_by_night) is int)
        self.assertTrue(type(my_model.latitude) is float)
        self.assertTrue(type(my_model.longitude) is float)
        self.assertTrue(type(my_model.amenity_ids) is list)
