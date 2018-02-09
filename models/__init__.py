#!/usr/bin/python3
"""
Creates a unique FileStorafe instance for my application
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
