import unittest
from datetime import datetime
from models.base_model import BaseModel
import time
import uuid


class TestBaseModel(unittest.TestCase):
    """
    This is test cases for BaseModel.
    """

    def setUp(self):
        """
        Seting up test environment
        """
        self.model = BaseModel()

    def test_instance(self):
        """
        Test if the instance is what is created.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_id_is_uuid(self):
        """
        Test if each instance is uuid.
        """
        testing_model = BaseModel()
        self.assertNotEqual(self.model.id, testing_model.id)

    def test_str_method(self):
        """
        Test the __str__ represention.
        """
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_to_dict_type(self):
        """
        Test the dict value type.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_to_save_method(self):
        """
        Test save method.
        """
        old_updated_at = self.model.updated_at
        time.sleep(0.1)  # Sleep to be sure updated_at is saved
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertGreater(new_updated_at, old_updated_at)

    def test_kwargs_creation(self):
        """
        Test kwargs in creating an instance.
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertEqual(new_model.__str__(), self.model.__str__())

    def test_kwargs_creation_not_in_class(self):
        """
        Test creating an instance with kwargs
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertNotIn('__class__', new_model.__dict__)

    def test_datetime_conversion(self):
        """
        Test if created_at and updated_at are converted to obj time
        """
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_id_is_a_string(self):
        """
        Test us id is a string
        """
        self.assertIsInstance(self.model.id, str)

    def test_updated_at_is_dateime(self):
        """
        Test is updated_at is a datetime object
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_created_at_is_datetime(self):
        """
        Test if created_at is a datetime object.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_created_at_is_equal_to_updated_at_on_creation(self):
        """
        Test whether created_at and updated_at are eqaul
        """
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_kwargs_creation_with_more_attributes(self):
        """
        Test additional attributes with kwargs.
        """
        model_dict = self.model.to_dict()
        model_dict['new_attr'] = 'new_value'
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.new_attr, 'new_value')


if __name__ == '__main__':
    unittest.main()
