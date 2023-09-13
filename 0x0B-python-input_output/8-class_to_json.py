#!/usr/bin/python3
""" module contains a function that returns the dictionary
description with simple data structure"""


def class_to_json(obj):
    """
    Returns the dictionary representation with simple data structure
    """
    result = obj.__dict__

    return result
