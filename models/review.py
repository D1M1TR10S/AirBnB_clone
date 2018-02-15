#!/usr/bin/python3
"""Review class for storing the user's reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Creating Review class that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
