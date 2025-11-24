#!/usr/bin/env python3
import cmd
"""The cmd module"""


class HBNBCommand(cmd.Cmd):
    """HBNB Cmd class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF for End of Life command: Ctl+D """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
