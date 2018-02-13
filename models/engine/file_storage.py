#!/usr/bin/python3
"""
FileStorage class - Converts a dictionary of objects to and from JSON format
in order to save past instances of a class.
"""
import json
import os.path
from models.base_model import BaseModel

class FileStorage:
    """
    Class that stores BaseModel dictionaries as json files
    Attributes:
    __file_path: path to the json file where dictionaries are stored
    __objects: a dictionary containing class name & id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        FileStorage.__objects['{}.{}'.format(
                              obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        d = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(d, f)


    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file exists; else, do nothing)
        eval(val['__class__'])(**val) is the same as BaseModel(**val)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as j_file:
                d = json.load(j_file)
            for key, val in d.items():
                self.__objects[key] = eval(val['__class__'])(**val)
