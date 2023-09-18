#!/usr/bin/python3
"""Defines class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overloading __str__ method.

        Returns:
            [Square] (<id>) <x>/<y> - <size> - in our case, width or height.
        """
        return f"[Square] {(self.id)} {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Returns the value of width"""
        return self.width

    @size.setter
    def size(self, new_value):
        """
    Sets the size of width and height

    Args:
        new_value: value to set to height and width
    """
        if not isinstance(new_value, int):
            raise TypeError("width must be an integer")
        elif new_value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = new_value
            self.height = new_value

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
