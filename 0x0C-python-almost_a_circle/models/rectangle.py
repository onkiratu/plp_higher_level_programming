#!/usr/bin/python3

"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the top-left corner of the rec    tangle.
         __y (int): The y-coordinate of the top-left corner of the rec    tangle.

    
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initilizing class attributes

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position
                (default is 0).
            y (int, optional): The y-coordinate of the rectangle's position
                (default is 0).
            id (int, optional): The ID of the rectangle (default is None).

        Raises:
            TypeError: If any of the arguments (width, height, x, or y) is not
                an integer.
            ValueError: If width or height is not greater than 0, or if x or y
                is less than 0.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

 
