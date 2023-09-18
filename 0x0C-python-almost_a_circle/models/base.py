#!/usr/bin/python3
"""module defines class Base"""


class Base:
    """This class will be the base of all other classes in thin project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        self.id = id
        if not id == None:
            Base.__nb_objects += 0
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

