#!/usr/bin/python3
"""
Converts a dictionary of objects to and from JSON format
in order to save past instances of a class.
"""
import json


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
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file exists; else, do nothing)
        """
        if (FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as j_file:
                FileStorage.__objects = json.load(j_file)
