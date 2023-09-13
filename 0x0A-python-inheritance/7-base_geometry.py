#!/usr/bin/python3
""" Defines a class BaseGeometry"""


class BaseGeometry:
    """
    Defines public instance methods:
        def area(self):
        def integer_validator(self, name, value):
    """
    def area(self):
        """
        computes area

        Raises:
            area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name: name of the value
            value: value to validate

        Raise:
            if value is not an integer: raise a TypeError exception,
            with the message <name> must be an integer
            if value is less or equal to 0: raise a ValueError
            exception with the message <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
