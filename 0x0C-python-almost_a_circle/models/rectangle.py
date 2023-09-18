#!/usr/bin/python3
"""Defines a class Rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initilizing class attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

#        if not isinstance(self.__height, int):
#            raise TypeError("height must be an integer")
#
#        if self.__height <= 0:
#            raise ValueError("height must be > 0")
#
#        if not isinstance(self.__width, int):
#            raise TypeError("width must be > 0")
#
#        if self.__width <= 0:
#            raise ValueError("width must be an integer")
#
#        if not isinstance(self.__x, int):
#            raise TypeError("x must be an integer")
#
#        if not isinstance(self.__y, int):
#            raise TypeError("y must be an integer")
#
#        if self.__x < 0:
#            raise ValueError("x must be >= 0")
#
#        if self.__y < 0:
#            raise ValueError("y must be >= 0")
#
    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets new value to width

        Args:
            value: value to set to width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets new value to height

        Args:
            value: value to set to height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets a new value to x

        Args:
            value: value to set to x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets new value to y

        Args:
            value: value to set to y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            self.__y = value

    def area(self):
        """
        Computes the area of the Rectangle instance

        Returns:
            Area of Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with character #"""
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            print("{}".format("#") * self.__width)

    def __str__(self):
        """Overides the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
