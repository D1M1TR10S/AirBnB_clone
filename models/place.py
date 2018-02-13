#!/usr/bin/python3
"""Module contains Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Describes the place.

    Attributes:
            city_id(str): City.id
            user_id(str): User.id
            name(str): name of place
            description(str): describe place
            number_rooms(int): how many rooms
            number_bathrooms(int): how many bathrooms
            max_guest(int): max guests allowed
            price_by_night(int): price/night
            latitude(float): latitude of place
            longitude(float): longitude of place
            amenity_ids(list): list of amenities(str)
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
