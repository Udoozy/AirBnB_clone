#!/usr/bin/env python3
import cmd
"""The cmd module"""


class HBNBCommand(cmd.Cmd):
    """HBNB Cmd class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
