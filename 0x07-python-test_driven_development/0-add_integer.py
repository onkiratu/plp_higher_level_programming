#!/usr/bin/python3
"""
This module holds a function for working with numbers
add_integer: adds two integers

"""


def add_integer(a, b=98):
    """
    This function adds two integers

    Args:
    a (int): first number
    b (int): second number

    Return:
    sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
