#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    THis is also a User Class that inhert Basemodel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
