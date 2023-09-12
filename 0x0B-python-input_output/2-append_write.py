#!/usr/bin/python3
"""
Module contains a function that appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the
    number of characters added.

    Args:
        filename: name of the file to append to
        text: text to append to the filename

    Return:
        number of character added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file = file.write(text)

    return len(text)
