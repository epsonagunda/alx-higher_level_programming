#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout """

def read_file(filename=""):
    """reads filename with utf-8"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
