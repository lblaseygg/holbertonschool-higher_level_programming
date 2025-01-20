#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        print(chr(ord(c) - 32) if 'a' <= c <= 'z' else c, end="")
    print()  # Ensure a new line is printed after the loop
