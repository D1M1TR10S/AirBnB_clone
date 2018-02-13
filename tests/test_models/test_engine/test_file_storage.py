#!/usr/bin/python3
"""Unittest for file storage."""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests file storage."""

    def test_type(self):
        """Check if attributes are correct type."""
        self.assertTrue(FileStorage.__file_path is str)
        self.assertTrue(FileStorage.__objects is dict)
