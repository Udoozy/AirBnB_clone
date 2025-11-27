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
    def __init__(self, *args, **kwargs):
        """Innitializing the atrributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String formated"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        """save mothod"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method that converts to dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()

        clean_dict = {}
        for key, value in obj_dict.items():
            clean_key = key.strip('"').strip("'")
            if isinstance(value, str):
                clean_value = value.strip('"').strip("'")
            else:
                clean_value = value
            clean_dict[clean_key] = clean_value
        return clean_dict
