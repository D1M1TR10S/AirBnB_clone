#!/usr/bin/python3
"""Test file for Place class"""
from unittest import TestCase
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(TestCase):
    """TestPlace class that checks the Place class for errors"""

    def setUp(self):
        """Creates the instance of Place"""
        self.place = Place()

    def tearDown(self):
        """Deletes the instance of Place"""
        del self.place

    def test_instance(self):
        """Checks if an instance exists"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Checks if public class attributes exists and are correct format"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_inheritance(self):
        """Checks if instance correctly inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
