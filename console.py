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
        args = arg.split()
        if self.check_args(args, 'create') == 0:
            new = classes[args[0]]()
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
        if self.check_args(args, 'show') == 0:
            print(storage.all()[args[0] + '.' + args[1]])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if self.check_args(args, 'destroy') == 0:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()

    def do_all(self, arg):
        """Prints string representations of all instances of a class"""
        args = arg.split()
        if self.check_args(args, 'all') == 0:
            print([str(value) for key, value in storage.all().items()
                  if arg in key])

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if self.check_args(args, 'update') == 0:
            key = '{}.{}'.format(args[0], args[1])
            setattr(storage.all()[key], args[2], args[3])

    @staticmethod
    def check_args(args, cmd):
        """Checks for proper usage."""
        if len(args) == 0:
            if cmd == 'all':
                print([str(value) for value in storage.all().values()])
            else:
                print('** class name missing **')
        elif args[0] not in classes:
            print('** class doesn\'t exist **')
        elif len(args) != 2:
            if cmd == 'all' or 'create':
                return 0
            else:
                print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in storage.all():
            print('** no instance found **')
        elif len(args) != 3 and cmd == 'update':
            print('** attribute name missing **')
        elif len(args) != 4 and cmd == 'update':
            print('** value missing **')
        else:
            return 0

if __name__ == '__main__':
    HBNBCommand().cmdloop()
