#!/usr/bin/python3
"""Test file for amenity class"""
from unittest import TestCase
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(TestCase):
    """TestAmenity class that checks the Amenity class for errors"""


    def setUp(self):
        """Creates an instance of Amenity"""
        self.amenity = Amenity()

    def tearDown(self):
        """Deletes an instance of Amenity"""
        del self.amenity

    def test_amenity_instance(self):
        """Checks if an instance of Amenity exists"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_attribute(self):
        """Checks if an attribute called name exists"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(type(self.amenity.name), str)

    def test_inheritance(self):
        """Checks if Amenity correctly inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))    
