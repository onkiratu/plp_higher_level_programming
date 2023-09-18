#!/usr/bin/python3

"""Rectangle module"""

from models.base import Base

class Rectangle(Base):
    """
    A class representing a rectangle, inheriting from the Base class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the top-left corner of the rectangle.
        __y (int): The y-coordinate of the top-left corner of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance.
            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int, optional): The x-coordinate of the top-left corner (default is 0).
                y (int, optional): The y-coordinate of the top-left corner (default is 0).
                id (int, optional): The unique identifier for the rectangle (default is None).

        width (property):
            Getter method for retrieving the width of the rectangle.

        width (setter):
            Setter method for setting the width of the rectangle.
            Args:
                value (int): The new width to set.
            Raises:
                ValueError: If the provided width is not greater than zero.

        height (property):
            Getter method for retrieving the height of the rectangle.

        height (setter):
            Setter method for setting the height of the rectangle.
            Args:
                value (int): The new height to set.
            Raises:
                ValueError: If the provided height is not greater than zero.

        x (property):
            Getter method for retrieving the x-coordinate of the rectangle's top-left corner.

        x (setter):
            Setter method for setting the x-coordinate of the rectangle's top-left corner.
            Args:
                value (int): The new x-coordinate to set.
            Raises:
                ValueError: If the provided x-coordinate is negative.

        y (property):
            Getter method for retrieving the y-coordinate of the rectangle's top-left corner.

        y (setter):
            Setter method for setting the y-coordinate of the rectangle's top-left corner.
            Args:
                value (int): The new y-coordinate to set.
            Raises:
                ValueError: If the provided y-coordinate is negative.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        # Call the constructor of the Base class and pass the id
        super().__init__(id)
        
        # Initialize private attributes
        self.__width = 0
        self.__height = 0
        self.__x = 0
        self.__y = 0
        
        # Use the setter methods to assign values, which also perform validation
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for the width attribute
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Validate that width is greater than zero
        if value <= 0:
            raise ValueError("Width must be greater than zero")
        self.__width = value

    # Getter and setter for the height attribute
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Validate that height is greater than zero
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    # Getter and setter for the x coordinate attribute
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        # Validate that x is non-negative
        if value < 0:
            raise ValueError("X coordinate must be non-negative")
        self.__x = value

    # Getter and setter for the y coordinate attribute
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        # Validate that y is non-negative
        if value < 0:
            raise ValueError("Y coordinate must be non-negative")
        self.__y = value

