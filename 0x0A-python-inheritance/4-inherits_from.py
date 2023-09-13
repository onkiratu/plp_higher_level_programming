#!/usr/bin/python3
""" Defines a function that checks whether an object is an
    instance of a class that inherited from a specifies class"""


def inherits_from(obj, a_class):
    """
    function that checks whether an object is an instance
    of a class that inherited from a specifies class

    Args:
        obj: object to check
        a_class: class to check
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
