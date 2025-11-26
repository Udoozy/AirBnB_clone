#!/usr/bin/env python3
"""
console.py: Entry point of commandline interpreter
"""
import cmd
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    """HBNB Commad interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the program (ctr+D / ctr+Z)"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints all the BaseModel Based on ID"""
        args = arg.split()

        if len(args) == 0:
            print("* class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist ** ")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = class_name + "." + obj_id

        all_obj = storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return
        print(all_obj[key])

    def do_destroy(self, arg):
        """This delets an Instance using its ID"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = class_name + "." + obj_id

        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        del (all_objs[key])

        storage.save()

    def do_all(self, arg):
        """Print all the string repr of all instance"""
        args = arg.split()

        if len(args) == 0:
            obj_list = [str(obj) for obj in storage.all().values()]
            print(obj_list)
            return

        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        obj_list = [str(obj) for obj in storage.all().values()
                    if obj.__class__.__name__ == class_name]

    def do_update(self, arg):
        """Update attritute by adding a new one"""
        args = arg.split()

        class_name = args[0]

        if len(args) == 0:
            print("** class name missing **")
            return

        if class_name not in classes:
            print("** class doesn't exist ** ")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = class_name + "." + obj_id
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2].strip('"').strip("'")

        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3].strip('"').split("'")

        if attr_value.isdigit():
            casted_value = int(attr_value)
        else:
            try:
                casted_value = float(attr_value)
            except ValueError:
                casted_value = attr_value.strip('"').strip("'")

        obj = all_objs[key]
        setattr(obj, attr_name, casted_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
