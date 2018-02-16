#!/usr/bin/python3
"""Command interpreter module."""

import cmd
import shlex
import re
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
            type_d = {'number_rooms': 'int', 'number_bathrooms': 'int',
                      'max_guest': 'int', 'price_by_night': 'int',
                      'latitude': 'float', 'longitude': 'float'}
            key = '{}.{}'.format(args[0], args[1])
            if args[2] in type_d:
                value = eval(type_d[args[2]])(args[3])
                setattr(storage.all()[key], args[2], value)
            else:
                setattr(storage.all()[key], args[2], args[3])
            storage.save()

    def do_count(self, arg):
        """Counts how many instances by class."""
        count = 0
        for value in storage.all().values():
            if value.__class__.__name__ == arg:
                count += 1
        print(count)

    def default(self, arg):
        """Default when command prefix not recognized."""
        s = (arg.replace('.', ' ').replace('(', ' ').replace(')', ' '))
        l = s.split()
        if len(l) > 1:
            cmd = l.pop(1)
        if '{' in s and cmd == 'update':
            s = s.replace('update', '')
            d = re.split(r"\s(?![^{]*})", s)
            for k, v in eval(d[3]).items():
                print(l[0]), print(l[1]), print(k), print(v)
                args = l[0] + ' ' + l[1][:-1] + ' ' + k + ' ' + str(v)
                self.do_update(args)
            return
        args = ' '.join(l).replace(',', '')
        try:
            eval('self.do_' + cmd + '(args)')
        except:
            print('Invalid argument.')

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
            if cmd == 'all' or cmd == 'create':
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
