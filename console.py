#!/usr/bin/python3
"""Command interpreter module."""

import cmd
from models.base_model import BaseModel
from models import storage

classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter."""
    prompt = '(hbnb) '

    def emptyline(self):
        """Overwrite emptyline method."""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel"""
        if self.check_args(arg) == 0:
            new = classes[arg[0]]()
            new.save()
            print('{}'.format(new.id))

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def do_show(self, arg):
        """Prints string representation"""
        args = arg.split()
        if self.check_args(args) == 0:
            print(storage.all()[args[0] + '.' + args[1]])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if self.check_args(args) == 0:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()

    def do_all(self, arg):
        """Prints string representations of all instances of a class"""
        if self.check_args(arg) == 0:
            obj_list = [str(value) for key, value in storage.all().items()
                        if arg in key]
            print('\n'.join([obj_str for obj_str in obj_list]))

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if self.check_args(args) == 0:

    @staticmethod
    def check_args(args):
        """Checks for proper usage."""
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in classes:
            print('** class doesn\'t exist **')
        elif len(args) != 2:
            print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in storage.all():
            print('** no instance found **')
        elif len(args) != 3:
            print('** attribute name missing **')
        elif len(args) != 4:
            print('** value missing **')
        else:
            return 0

if __name__ == '__main__':
    HBNBCommand().cmdloop()
