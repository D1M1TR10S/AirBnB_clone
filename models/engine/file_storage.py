#!/usr/bin/python3
"""File storage module."""
import json
import os.path


class FileStorage:
    """File storage engine.

    Attributes:
    __file_path: file path containing object json string
    __objects: dictionary of objects saved
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary of objects."""
        return (FileStorage.__objects)

    def new(self, obj):
        """Adds new object to __objects."""
        FileStorage.__objects['{}.{}'.format(
                              obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves an instance in json format."""
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """Deserializes json string."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
