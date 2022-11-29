#!/usr/bin/python3
for low in range(26):
    if low != 4 and low != 16:
        print("{:s}".format(chr(low + ord("a"))), end="")
