#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1  # Subtract 1 because the first argument is the script name
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{argc} arguments:")
        for i in range(1, argc + 1):
            print(f"{i}: {sys.argv[i]}")
