#!/usr/bin/python3
"""Unittest for file storage."""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests file storage."""

    def test_privacy(self):
        """Check if attributes are private."""
        a = FileStorage()
        with self.assertRaises(AttributeError):
            print(a.file_path)
        with self.assertRaises(AttributeError):
            print(a.objects)
