#!/usr/bin/python3
for k in range(0, 10):
    for l in range(1, 10):
        if k >= l:
            continue
        elif k == 8 and l == 9:
            print("{}{}".format(k, l))
        else:
            print("{}{}, ".format(k, l), end="")
