#!/usr/bin/python3
"""
Command line interpreter for HBnB console
"""
import cmd
import models
import json
import shlex
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB Command class with custom prompt and shell methods
    """
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it to json file and prints the id
        Prints errors if the class name is missing
        or class does not exist.
        """
        args = shlex.split(arg)
        if len(args) == 1:
            if exists(args[0]):
                new = models.class_dict[args[0]]()
                new.save()
                print(new.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Shows a dictionary of an instance of
        a class based on class name and id
        """
        args = arg.split()
        if len(args) > 0:
            if exists(args[0]):
                if len(args) == 2:
                    class_id = "{}.{}".format(args[0], args[1])
                    temp_d = models.storage.all()
                    if class_id in temp_d:
                        print(temp_d[class_id])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Deletes a dictionary of an instance of
        a class from the json file based on
        class name and id
        """
        args = arg.split()
        deleted = 0
        if len(args) > 0:
            if exists(args[0]):
                if len(args) == 2:
                    obj_id = "{}.{}".format(args[0], args[1])
                    obj = models.storage.all()
                    for key, value in obj.items():
                        if key == obj_id:
                            obj.pop(key)
                            deleted = 1
                            break
                    if deleted == 0:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")
        models.storage.save()
    
    def do_all(self, arg):
        """
        Prints string representations of all instances
        based or not on the class name
        """
        arg = arg.split()
        class_list = []
        all_objs = models.storage.all()
        if len(arg) == 1:
            """class name is given as an argument
            """
            if exists(args[0]):
                for key, value in all_objs.items():
                    if arg[0] == key:
                        class_list.append(value)
        elif len(arg) == 0:
            """class name is not given
            """
            for key, value in all_objs.items():
                class_list.append(value)
        print(class_list)

    def do_update(self, arg):
        """
        Updates an attribute in the
        class and saves to json file
        """
        args = arg.split()
        if len(args) > 0:
            if exists(args[0]):
                if len(args) > 1:
                    if len(args) > 2:
                        if len(args) > 3:
                            obj_id = "{}.{}".format(args[0], args[1])
                            obj = models.storage.all()
                            if obj_id in obj:
                                instance = obj[obj_id]
                                setattr(instance, args[2], args[3])
                                models.storage.save()
                            else:
                                print("** no instance found **")
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline():
        """Does nothing if line is empty
        """
        pass


def exists(arg):
    """Checks to see if an instance exists
    """
    if arg in models.class_dict:
        return True
    else:
        print("** class doesn't exist **")
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
