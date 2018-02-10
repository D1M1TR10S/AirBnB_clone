#!/usr/bin/python3
"""
Base Model class for all the common attributes and methods
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
    Base class for AirBnB console
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing class Instance
        """
        self.id = str(uuid.uuid4())
        if (kwargs):
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                self.created_at = datetime.strptime(
                    self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
                self.updated_at = datetime.strptime(
                    self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                storage.new(self)
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

    def __str__(self):
        """
        Printing Attribute information to stdout
        """
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Saves 'updated_at' with the current date and time
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of instance __dict__
        """
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)
