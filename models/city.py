#!/usr/bin/python3
"""City class for storing user's city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Creating City class that inherits from BaseModel
    """

    state_id = ""
    name = ""
