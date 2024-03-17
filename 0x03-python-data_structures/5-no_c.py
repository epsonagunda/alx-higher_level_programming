#!/usr/bin/python3
def no_c(my_string):
    chars_string = ""
    for c in my_string:
        if c not in "Cc":
            chars_string += c
    return chars_string
