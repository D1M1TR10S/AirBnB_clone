#!/usr/bin/python3
"""Test file for Review class"""
from unittest import TestCase
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(TestCase):
    """TestReview class that checks the Review class for errors"""


    def setUp(self):
        """Creates the instance of Place"""
        self.review = Review()

    def tearDown(self):
        """Deletes the instance of Place"""
        del self.review

    def test_instance(self):
        """Checks if an instance exists"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Checks if public class attributes exists and are correct format"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_inheritance(self):
        """Checks if instance correctly inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
