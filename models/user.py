#!/usr/bin/python3
"""User class for storing information about the user
"""


class User(BaseModel):
    """Creating user class that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
