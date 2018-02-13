#!/usr/bin/python3
"""
Initializes package.
Creates a unique FileStorage instance for my application
"""
from models.engine.file_storage import FileStorage
from .base_model import BaseModel

class_dict = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
