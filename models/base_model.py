#!/usr/bin/python3
"""
Module for AirBnB clone
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Basemodel for all the classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializing the AirBnb class
        """

        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for i, j in kwargs.items():
                if i in ("updated_at", "created_at"):
                    self.__dict__[i] = datetime.strptime(j, date_format)
                elif i[0] == "id":
                    self.__dict__[i] = str(j)
                else:
                    self.__dict__[i] = j

    def __str__(self):
        """
        Returns it string repr
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updaate the  updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys and value
        """
        my_dict = {}
        for i, j in self.__dict__.items():
            if i == "created_at" or i == "updated_at":
                my_dict[i] = j.isoformat()
            else:
                my_dict[i] = j
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
