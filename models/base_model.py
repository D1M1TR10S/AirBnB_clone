#!/usr/bin/python3
"""Base Model class for all the common attributes and methods
"""
import datetime


class BaseModel:
	"""Base class for AirBnB console
	"""
	def __init__(self):
		"""Initializing class Instance
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = ## Need to add tie in which an object is updated
		
