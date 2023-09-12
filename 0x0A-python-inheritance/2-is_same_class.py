#!/usr/bin/python3
"""
This module contains a a function that chacks instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks instance of a class

    Args:
        obj: object to check
        a_class: class to check

    Return:
        True if obj belong tp a_class
        Otherwise False
    """
    return type(obj) == a_class
