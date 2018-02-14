#!/usr/bin/python3
"""
FileStorage class - Converts a dictionary of objects to and from JSON format
in order to save past instances of a class.
"""
import json
import os.path
import models


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
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects['{}.{}'.format(
                       obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        Using dict comprehension to turn objects from self.__objects
        into a dict
        """
        d = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, mode='w') as f:
            json.dump(d, f)


    def reload(self):
        """
        deserializes the JSON file back into __objects
        (only if the JSON file exists; else, do nothing)
        Sends objects to BaseModel as keyword arguments:
        models.class_dict[uni](**val) same as BaseModel(**val)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r') as j_file:
                d = json.load(j_file)
            for key, val in d.items():
                uni = val.get('__class__')
                if uni in models.class_dict:
                    self.__objects[key] = models.class_dict[uni](**val)
