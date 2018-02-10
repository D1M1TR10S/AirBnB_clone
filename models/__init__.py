#!/usr/bin/python3
"""
Initializes package.
Creates a unique FileStorage instance for my application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
