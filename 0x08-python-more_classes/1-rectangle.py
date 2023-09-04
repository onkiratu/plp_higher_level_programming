#!/usr/bin/python3
"""
This module contains a class  that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize an instance of Rectangle

        Args:
        self.__width: width of the rectangle
        self.__height: height of the rectanle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get te value of the width

        Returns:
            The current value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of width

        Args:
            value: value to assign to width

        Raises:
            TypeError: if the value is not an integer
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Get the value of height

        Returns:
            The current value of height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the valu of height

        Args:
            value: value to assign to height

        Raises:
            TypeError: if the value is not an integer
            ValueError: if value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
