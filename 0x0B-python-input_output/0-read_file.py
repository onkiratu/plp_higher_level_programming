#!/usr/bin/python3
"""
This module contains a function that reads data and print to stdout
"""


def read_file(filename=""):
    """
    Reads text file and prints it to stdout

    Args
        filename: name of the file to read from
    """

    with open(filename, mode='r', encoding='utf-8') as file:
        file = file.read()
        for line in file:
            print(line, end='')
