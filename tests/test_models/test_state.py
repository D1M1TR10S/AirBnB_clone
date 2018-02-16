#!/usr/bin/python3
"""Test file for State class"""
from unittest import TestCase
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(TestCase):
    """TestState class that checks the State class for errors"""

    def setUp(self):
        """Creates the instance of State"""
        self.state = State()

    def tearDown(self):
        """Deletes the instance of State"""
        del self.state

    def test_instance(self):
        """Checks if an instance exists"""
        self.assertIsInstance(self.state, State)

    def test_name_attribute(self):
        """Checks if an attribute called name exists"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(type(self.state.name), str)

    def test_inheritance(self):
        """Checks if instance correctly inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
