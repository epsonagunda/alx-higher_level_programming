#!/usr/bin/python3
"""define to_json"""
class Student:
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Class Dictionary """
        return self.__dict__.copy()
