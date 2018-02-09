#!/usr/bin/python3
"""
Base Model class for all the common attributes and methods
"""
from datetime import datetime
import uuid


class BaseModel:
	"""
	Base class for AirBnB console
	"""

	def __init__(self):
		"""
		Initializing class Instance
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()

	def __str__(self):
        	"""
		Printing Attribute information to stdout
        	"""
        	return("[{}] ({}) {}".format
              		(self.__class__.__name__, self.id, self.__dict__))

	def save(self):
		"""
		Saves the date and time of each change to object
		"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""
		Returns a dictionary containing all keys/values of __dict__ of the instance
		"""
		my_dict = self.__dict__
		my_dict['__class__'] = self.__class__.__name__
		my_dict['created_at'] = self.created_at.isoformat()
		my_dict['updated_at'] = self.updated_at.isoformat()
		return (my_dict)
