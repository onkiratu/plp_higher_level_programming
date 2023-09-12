#!/usr/bin/python3
""" creates an object from Json file"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        data = file.read()
        obj = json.loads(data)

    return obj
