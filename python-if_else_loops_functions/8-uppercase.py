#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            print("{:c}".format(ord(letter) - 32), end="")
        else:
            print("{:c}".format(ord(letter)), end="")
    print()
