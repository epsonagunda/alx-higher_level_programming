#!/usr/bin/python3
"""
Print Square module, for printing squares with "#".

useful for all square-based applications
"""
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("x" * size)
