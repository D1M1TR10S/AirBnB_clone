#!/usr/bin/python3
"""
Base Model class for all the common attributes and methods
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Base class for AirBnB console
    Uses cmd module
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing class Instance
        
        if: kwargs are received then we set class attributes
        with keys and values from reloaded datetimes
        
        else: Set created_at and updated_at to current datetime,
        send objects of class to storage.new, and save the dict
        to a json file.
        """
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
            
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        Printing Class information to stdout
        """
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Saves 'updated_at' with the current date and time
        Saves the current class in FileStorage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of instance __dict__
        Converts datetime to isoformat for json compliance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)
