#!/usr/bin/python3
""" This module defines a JSON to string function"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a json string
    """

    return json.loads(my_str)
