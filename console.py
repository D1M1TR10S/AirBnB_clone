#!/usr/bin/python3
<<<<<<< HEAD
"""Command interpreter module."""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Command interpreter."""
    prompt = '(hbnb) '

    def emptyline(self):
        """Overwrite emptyline method."""
        pass

    def do_create(self, arg):
        """Creates new instance"""
        args = shlex.split(arg)
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
        args = shlex.split(arg)
        if self.check_args(args, 'show') == 0:
            print(storage.all()[args[0] + '.' + args[1]])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if self.check_args(args, 'destroy') == 0:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()

    def do_all(self, arg):
        """Prints string representations of all instances of a class"""
        args = shlex.split(arg)
        if self.check_args(args, 'all') == 0:
            print([str(value) for key, value in storage.all().items()
                  if args[0] in key])

    def do_update(self, arg):
        """Updates an instance."""
        args = shlex.split(arg)
        if self.check_args(args, 'update') == 0:
            to_int = {'number_rooms', 'number_bathrooms',
                      'max_guest', 'price_by_night'}
            to_float = {'latitude', 'longitude'}
            key = '{}.{}'.format(args[0], args[1])
            if args[2] in to_int:
                setattr(storage.all()[key], args[2], int(args[3]))
            elif args[2] in to_float:
                setattr(storage.all()[key], args[2], float(args[3]))
            elif args[2] == 'amenity_ids':
                setattr(storage.all()[key], args[2], [args[3]])
            else:
                setattr(storage.all()[key], args[2], args[3])
            storage.save()

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
        elif len(args) < 2:
            if cmd == 'all' or 'create':
                return 0
            else:
                print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in storage.all():
            print('** no instance found **')
        elif len(args) < 3 and cmd == 'update':
            print('** attribute name missing **')
        elif len(args) < 4 and cmd == 'update':
            print('** value missing **')
        else:
            return 0
=======
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
>>>>>>> 467f7e2bdacb2b2b26dd5afce310c0da71cec664

if __name__ == '__main__':
    HBNBCommand().cmdloop()
