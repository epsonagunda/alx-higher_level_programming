#!/usr/bin/python3
for k in range(0, 10):
    for l in range(k + 1, 10):
        if k == 8 and l == 9:
            print("89")
        else:
            print("{}{}, ".format (k, l), end="")
