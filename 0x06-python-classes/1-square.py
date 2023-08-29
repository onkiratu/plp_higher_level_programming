#!/usr/bin/python3
"""This module creates class Square"""


class Square:
    """
    This Square class defines a square.

    Attributes:
        size (int): The size of square
    """

    def __init__(self, size):
        """
        Args:
            size (int): the size of the square.

        Attributes:
            _size (int): the size of the square.
        """
        self.__size = size
