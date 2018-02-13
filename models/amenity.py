#!/usr/bin/python3
"""Module contains Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Describes amenities.

    Attributes:
            name(str): name of amenity
    """

    name = ''
