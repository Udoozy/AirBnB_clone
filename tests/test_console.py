import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand.
    """

    def setUp(self):
        """
        Seting up test environment.
        """
        storage._FileStorage__objects = {}
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clearing test environment.
        """
        storage._FileStorage__objects = {}

    def test_create(self):
        """
        Creating command for various test.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            model_id = fake_out.getvalue().strip()
            self.assertIn(f"BaseModel.{model_id}", storage.all())

            self.console.onecmd("create User")
            user_id = fake_out.getvalue().strip().split('\n')[-1]
            self.assertIn(f"User.{user_id}", storage.all())

            self.console.onecmd("create City")
            city_id = fake_out.getvalue().strip().split('\n')[-1]
            self.assertIn(f"City.{city_id}", storage.all())

            self.console.onecmd("create State")
            state_id = fake_out.getvalue().strip().split('\n')[-1]
            self.assertIn(f"State.{state_id}", storage.all())

            self.console.onecmd("create Amenity")
            amenity_id = fake_out.getvalue().strip().split('\n')[-1]
            self.assertIn(f"Amenity.{amenity_id}", storage.all())

            self.console.onecmd("create Place")
            place_id = fake_out.getvalue().strip().split('\n')[-1]
            self.assertIn(f"Place.{place_id}", storage.all())

            self.console.onecmd("create Review")
            review_id = fake_out.getvalue().strip().split('\n')[-1]
            self.assertIn(f"Review.{review_id}", storage.all())

    def test_show(self):
        """
        Showing command for various models.
        """
        d_bmd = BaseModel()
        d_bmd.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show BaseModel {d_bmd.id}")
            output = fake_out.getvalue().strip()
            self.assertIn(d_bmd.id, output)

    def test_destroy(self):
        """
        Test to destroy command for various models.
        """
        d_bmd = BaseModel()
        d_bmd.save()
        d_bmd_id = d_bmd.id
        self.assertIn(f"BaseModel.{bm_id}", storage.all())
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy BaseModel {bm_id}")
            self.assertNotIn(f"BaseModel.{bm_id}", storage.all())

    def test_all(self):
        """
        Test all command on various models.
        """
       d_ bmd = BaseModel()
        d_bmd.save()
        user = User()
        user.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            output = fake_out.getvalue().strip()
            self.assertIn(f"BaseModel.{d_bmd.id}", output)
            self.assertIn(f"User.{user.id}", output)

    def test_update(self):
        """
        Test update command on various models.
        """
        d_bmd = BaseModel()
        d_bmd.save()
        d_bmd_id = d_bmd.id
        with patch('sys.stdout', new=StringIO()):
            self.console.onecmd(f"update BaseModel {d_bmd_id} name 'Test'")
            self.assertEqual(storage.all()[f"BaseModel.{d_bmd_id}"].name, 'Test')


if __name__ == '__main__':
    unittest.main()
