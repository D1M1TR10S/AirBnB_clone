#!/usr/bin/python3
"""Unittest for base model."""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Tests Base Model."""

    def test_type(self):
        """Checks type of attributes."""
        my_model = BaseModel()
        self.assertTrue(type(my_model.id) is str)
        self.assertTrue(type(my_model.to_dict()['created_at']) is str)
        self.assertTrue(type(my_model.to_dict()['updated_at']) is str)

    def test_kwargs(self):
        """Make sure kwargs set instance's attributes"""
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        new_model = BaseModel(**my_dict)
        self.assertEqual(my_model.id, new_model.id)
        self.assertFalse(my_model is new_model)
        self.assertTrue(type(my_model.created_at) is datetime.datetime)
        self.assertTrue(type(new_model.created_at) is datetime.datetime)
