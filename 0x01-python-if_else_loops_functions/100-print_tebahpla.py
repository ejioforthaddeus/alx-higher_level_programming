#!/usr/bin/python3
max_upper = 90
max_lower = 122
for i in range(0, 13):
    max_upper -= 1
    print("{}{}".format(chr(max_lower), chr(max_upper)), end="")
    max_upper -= 1
    max_lower -= 2
