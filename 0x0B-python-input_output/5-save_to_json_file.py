#!/usr/bin/python3
""" Defines a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation
    
    Args:
        my_obj: object to be written into the file
        filename: name of the file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
