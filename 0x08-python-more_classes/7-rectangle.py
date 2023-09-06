#!/usr/bin/python3
"""
This module contains a class  that defines a rectangle

functions:
        width(self)
        width(self, value)
        height(self)
        height(self, value)
"""


class Rectangle:
    """
    This class defines a rectangle
    number_of_instances = 0
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize an instance of Rectangle

        Args:
        self.__width: width of the rectangle
        self.__height: height of the rectanle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Calculates the area of a rectangle

        Returns:
            The rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle

        Returns:
            The rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Prints a rectangle with the character #

        Returns:
            Rectangle
        """
        rect = ""

        if self.width == 0 or self.height == 0:
            return rect
        else:
            for rows in range(self.height):
                for elements in range(self.width):
                    rect += "#"
                if rows < self.height - 1:
                    rect += '\n'
        return rect

    def __repr__(self):
        """
        Returns a string representation of the rectangle

        Return:
        str: A string representation in the format Rectangle(2, 4)
        """
        return "Rectangle(2, 4)"

    def __del__(self):
        """
        Prints message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
