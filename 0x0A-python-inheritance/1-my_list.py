#!/usr/bin/python3
"""
This module contains MyList class that inherits from list
"""


class MyList(list):
    """
    A class Mylist that inherits from list
    """

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        """
        list1 = []

        sorted_list = sorted(self)
        for item in sorted_list:
            list1.append(item)

        print(list1)
