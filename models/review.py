#!/usr/bin/python3
"""Review class for storing the user's reviews
"""


class Review(BaseModel):
    """Creating Review class that inherits from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
