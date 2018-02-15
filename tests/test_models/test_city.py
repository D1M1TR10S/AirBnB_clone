#!/usr/bin/python3
"""Test file for City class"""
from unittest import TestCase
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(TestCase):
    """TestCity class that checks the City class for errors"""


    def setUp(self):
        """Creates the instance of City"""
        self.city = City()

    def tearDown(self):
        """Deletes the instance of City"""
        del self.city

    def test_instance(self):
        """Checks if an instance exists"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Checks if public class attributes exists"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(type(self.city.state_id), str)
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(type(self.city.name), str)

    def test_inheritance(self):
        """Checks if instance correctly inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))    
