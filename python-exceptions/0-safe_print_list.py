#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Tracks successfully printed elements
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1  # Increment count for each printed element
    except IndexError:
        pass  # Handle out-of-range gracefully
    finally:
        print()  # Print a newline after printing all elements
        return count  # Return the count of printed elements
