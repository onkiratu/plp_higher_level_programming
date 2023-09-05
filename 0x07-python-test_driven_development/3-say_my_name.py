#!/usr/bin/python3
"""
This module contains a function that prints a name.
Function: say_my_name(first_name, last_name="")
"""

def say_my_name(first_name, last_name=""):
    """
    This functions prints a name

    Args:
    first_name (string): first name to print
    second_name (string): second name to print

    Return:
    string: A string containing a name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))

