#!/usr/bin/python3
"""
Command line interpreter for HBnB console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB Command class with custom prompt and shell methods
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
