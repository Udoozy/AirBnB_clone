#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is review class that inherit from BaseClass.
    """
    place_id = ""
    user_id = ""
    text = ""
