#!/usr/bin/python3
"""Square module"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiated size attribute"""
        self.__size = size
        self.__position = position

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            symbol = "#"
            symbol1 = "_"
            for row in range(self.__size):
                print(end=f"{symbol1}" * self.__position[0])
                print(f"{symbol}" * self.__size)

    @property
    def position(self):
        """returns position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position values"""
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
