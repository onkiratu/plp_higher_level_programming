#!/usr/bin/python3
"""
module contains a function that writes a string to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters writen.

    Args
        filename: file to be writen
        text: string to be written

    Return:
        number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file = file.write(text)

    return len(text)
