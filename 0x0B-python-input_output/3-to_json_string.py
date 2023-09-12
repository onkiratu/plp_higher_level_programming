#!usr/bin/python3
"""
module contains a function that returns a JSON rep of an object
"""
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object(string).

    Args:
        my_obj: object to return the rep of

    Return:
        JSON rep of my_obj
    """
    return json.dumps(my_obj)
