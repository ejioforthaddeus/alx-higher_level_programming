#!/usr/bin/python3
def uppercase(str):
    for x in str:
        num = ord(x)
        if (num >= 97 and num <= 122):
            upper = chr((num - 97) + 65)
        else:
            upper = x
        print("{}".format(upper), end="")
    print("")
