#!/usr/bin/python3
"""Module contains City class."""
from models.base_model import BaseModel 


class City(BaseModel):
	"""City class.

	state_id(str): State.id
	name(str): name of city
	"""

	state_id = ''
	name = ''
