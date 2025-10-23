#!/usr/bin/python3
"""
Module for AirBnB clone
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Basemodel for all the classes
    """
    def __init__(self):
        """Innitializing the atrributes"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String formated"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"
  
    def save(self):
        """save mothod"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method that converts to dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
