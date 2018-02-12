#!/usr/bin/python3
"""Module containing base model."""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Base model that other objects will inherit from.

	Attributes:
		id: ID of the object.
		created_at: datetime of instance creation
		updated_at: datetime instance was updated
    """

    def __init__(self, *args, **kwargs):
        """Constructor method."""
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
                storage.new(self)
                self.created_at = datetime.today()
                self.updated_at = datetime.today()

    def __str__(self):
        """String representation of object."""
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Saves instance to dictionary, updates datetime."""
        storage.save()
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary representation of object."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)
