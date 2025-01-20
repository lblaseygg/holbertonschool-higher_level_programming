#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':  # check if the character is lowercase
            print(chr(ord(c) - 32), end="")  # convert lowercase to uppercase
        else:
            print(c, end="")  # print non-lowercase characters as is
    print()  # ensure there's a newline at the end
