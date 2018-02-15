#!/usr/bin/python3
"""Unit tests for BaseModel class
"""
from unittest import TestCase
from io import StringIO
import os
import sys
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(TestCase):
    """BaseModelTest class where BaseModel is tested for errors
    """

    def setUp(self):
        """Creates an instance of BaseModel"""
        self.base = BaseModel()

    def tearDown(self):
        """Delete an instance of BaseModel"""
        del self.base

    def test_kwargs(self):
        """Make sure kwargs set instance's attributes"""
        my_dict = self.base.to_dict()
        new_model = BaseModel(**my_dict)
        self.assertEqual(self.base.id, new_model.id)
        self.assertFalse(self.base is new_model)
        self.assertTrue(type(self.base.created_at) is datetime)
        self.assertTrue(type(new_model.created_at) is datetime) 

    def test_base_instance(self):
        """Checks if instance is created"""
        self.assertIsInstance(self.base, BaseModel)

    def test_base_created_time(self):
        """Checks if created_at attribute exists"""
        self.assertTrue(hasattr(self.base, "created_at"))

    def test_base_created_type(self):
        """Checks if created_at is correct type"""
        self.assertEqual(type(self.base.updated_at), datetime)

    def test_base_updated_time(self):
        """Checks if updated_at attribute exists"""
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_base_updated_type(self):
        """Checks if updated_at is correct type"""
        self.assertEqual(type(self.base.updated_at), datetime)

    def test_base_id(self):
        """Checks if id attribute exists"""
        self.assertTrue(hasattr(self.base, "id"))

    def test_base_id_type(self):
        """Checks if id is type string"""
        self.assertEqual(type(self.base.id), str)

#    def test_base_str(self):
#        """Checks if string representation is correct"""
#        result = StringIO()
#        sys.stdout = result
#        print(self.base)
#        self.assertEqual(result, "[{}] ({}) {}".format(\
#        self.base.__class__.__name__, self.base.id, self.base.__dict__))

    def test_save(self):
        """Checks if save method works"""
        self.base.save()
        with open('file.json', mode='r') as f:
            d = json.load(f)
        self.assertTrue("{}.{}".format(\
                self.base.__class__.__name__, self.base.id) in d)

    def test_base_to_dict(self):
        """Checks if to_dict method works"""
        test_dict = self.base.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue(self.base.id in test_dict['id'])
        test_created = self.base.created_at.isoformat()
        test_updated = self.base.updated_at.isoformat()
        self.assertTrue(test_dict['created_at'] == test_created)
        self.assertTrue(test_dict['updated_at'] == test_updated)
        self.assertEqual(type(test_dict['created_at']), str)
        self.assertEqual(type(test_dict['updated_at']), str)
