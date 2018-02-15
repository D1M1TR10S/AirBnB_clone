#!/usr/bin/python3
"""Unittest for file storage."""
import unittest
import os.path
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests file storage."""

    def test_privacy(self):
        """Check if attributes are private."""
        a = FileStorage()
        with self.assertRaises(AttributeError):
            print(a.file_path)
        with self.assertRaises(AttributeError):
            print(a.objects)

    def test_type(self):
        """Check if methods return expected type."""
        a = FileStorage()
        self.assertTrue(type(a.all()) is dict)

    def test_new(self):
        """Tests if new method adds obj to __objects."""
        a = FileStorage()
        b = BaseModel()
        a.new(b)
        self.assertTrue('BaseModel.' + b.id in a.all())

    def test_save(self):
        """Tests that save method does what I told it to do."""
        a = FileStorage()
        a.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Make sure __objects is reloaded properly."""
        a = FileStorage()
        a.save()
        a.reload()
        for values in a.all().values():
            self.assertTrue(values is not dict)
