#!/usr/bin/python3
"""defining from_json_string"""
import json


def from_json_string(my_str):
    """ function that returns an Python data represented by a JSON """
    return json.loads(my_str)
