#!/usr/bin/python3
"""
Command line interpreter for HBnB console
"""
import cmd
import models


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

        if present('class name', arg):
            if exists(arg):
                new = models.class_dict[arg]()
                new.save()
                print(new.__class__.__name__, new.id)

    def do_show(self, arg):
        """
        Shows a dictionary of an instance of
        a class based on class name and id
        """
        args = arg.split()
        # Fix error check to account for missing arguments
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if present('class name', args[0]):
            if exists(args[0]):
                if present('instance id', args[1]):
                    class_id = "{}.{}".format(args[0], args[1])
                    temp_d = models.storage.all()
                    if class_id in temp_d:
                        print(temp_d[class_id])
                    else:
                        print("** no instance found **")

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

def present(name, arg):
    """Checks to see if an argument is present
    """
    if arg is not "":
        return True
    else:
        print("** {} missing **".format(name))
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
