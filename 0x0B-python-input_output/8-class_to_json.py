!/usr/bin/python3
"""define class_to_json function"""

def class_to_json(obj):
    """ function that returns the dictionary
    description
    """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
