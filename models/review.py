#!/usr/bin/python3
"""Module contains City class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review info.

    Attributes:
            place_id(str): Place.id
            user_id(str): User.id
            text(str): a string
    """

    place_id = ''
    user_id = ''
    text = ''
