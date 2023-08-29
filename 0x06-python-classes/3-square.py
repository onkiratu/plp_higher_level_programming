#!/usr/bin/python3
""" This module creates a square class """


class Square:
    """
    This square class defines a square

    Attributes:
        size: size of one side of the square
    """
    def __init__(self, size=0):
        """
        Args:
            size: size of one side of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        This method returns the current square area
        """
        return self.__size**2
