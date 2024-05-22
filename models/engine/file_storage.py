#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes and deserializes JSON FILE
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dict version
        """
        return self.__objects

    def new(self, obj):
        """
        Sets THE __object with obj id
        """
        j = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[j] = obj

    def save(self):
        """
        Serializes __objects to the JSON file with d right path.
        """
        obj_dict = {j: obj.to_dict() for j, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as File:
            json.dump(obj_dict, File)

    def reload(self):
        """
        Deserializes the JSON file to __objects but if the file exists
        """
        try:
            with open(self.__file_path, 'r') as File:
                obj_dict = json.load(File)
                for i, j in obj_dict.items():
                    cls_name = j['__class__']
                    self.__objects[i] = globals()[cls_name](**j)
        except FileNotFoundError:
            pass
