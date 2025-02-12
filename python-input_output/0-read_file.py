#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and prints it out to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
