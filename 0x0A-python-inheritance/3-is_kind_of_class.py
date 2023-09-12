#!/usr/bin/python3
"""
This module contains a function that test class instances
"""


def is_kind_of_class(obj, a_class):
    """
    This function tests for an object of a class

    Args:
    obj: object to test
    a_class: class to test against

    Return:
        True if the object is an instance of
            or ab obect is an instance of a class
        Otherwise returns False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
