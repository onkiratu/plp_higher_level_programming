#!/usr/bin/python3
"""
This module holds a function that prints a square with the character #.
Function: print_square(size)
"""

def print_square(size):
    """
    This function print a square with the character #

    Args:
    size (int): size length of the square

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for symbol in range(size):
            print(end="{}".format("#"))
        print()
