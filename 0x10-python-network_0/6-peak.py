#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """
def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
