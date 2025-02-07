#!/usr/bin/python3
class MyList(list):
    """
    A subclass of list that includes a method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order without modifying the original list.
        """
        print(sorted(self))  # Uses sorted() to avoid modifying self
