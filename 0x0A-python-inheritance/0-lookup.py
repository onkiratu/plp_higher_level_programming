#!/usr/bin/python3
"""
This module contains a function that return attributes and methods of an abject
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Return:
        Attributes and methods
    """

    my_object = obj
    attr_and_methods = dir(my_object)

    return attr_and_methods
