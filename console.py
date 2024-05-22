#!/usr/bin/python3

"""
Command line interface for BnB
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command intepreter for HBNBComman.
    """

    prompt = '(hbnb) '

    def do_exit(self, arg):
        """
        exit command to terminate prompt.
        """
        return True

    def do_EOF(self, arg):
        """
        End of FIle proces.
        """
        print()
        return True

    def emptyline(self):
        """
        pass empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel,
        User, State, City, Amenity, Place, or Review,
        saves it, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show an instance based on class id and name.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Destroy an instance based on class.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Show all instances of  all classes.
        """
        if arg and arg not in globals():
            print("** class doesn't exist **")
            return
        instance = storage.all()
        if arg:
            instance = {key: val for key, val in instance.items()
                         if key.startswith(arg)}
        print([str(obj) for obj in instance.values()])

    def do_update(self, arg):
        """
        Update an instance based on id and name
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        an_instance = storage.all()[key]
        setattr(an_instance, args[2], args[3])
        an_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
