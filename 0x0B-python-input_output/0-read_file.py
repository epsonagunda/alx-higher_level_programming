#!/usr/bin/python3
"""a function that read a text file"""

def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
