#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    add = a + b
    sub = a - b
    div = a / b
    mul = a * b
    print("{} + {} = {}".format(a, b, add))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, mul))
    print("{} / {} = {}".format(a, b, div))
