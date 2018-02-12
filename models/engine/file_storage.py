#!/usr/bin/python3
"""File storage module."""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to __objects."""
        FileStorage.__objects['{}.{}'.format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves an instance in json format."""
        d = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(d, f)

    def reload(self):
        """Deserializes json string."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                d = json.load(f)
            for k, v in d.items():
                self.__objects[k] = eval(v['__class__'])(**v)
