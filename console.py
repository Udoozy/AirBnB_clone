#!/usr/bin/env python3
import cmd
"""
console.py: Entry point of commandline interpreter
"""


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
