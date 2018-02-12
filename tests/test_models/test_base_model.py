#!/usr/bin/python3
"""Unittest for base model."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests Base Model."""
    
    def test_type(self):
        """Checks type of attributes."""
        my_model = BaseModel()
        self.assertIs(my_model.id, str)
