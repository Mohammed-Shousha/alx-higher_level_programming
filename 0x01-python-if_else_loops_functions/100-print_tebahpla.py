#!/usr/bin/python3
for i in range(26):
    print("{}".format(chr((90 - i) if i % 2 else 122 - i)), end="")
