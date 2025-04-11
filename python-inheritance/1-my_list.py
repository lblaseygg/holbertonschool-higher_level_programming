#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""

class MyList(list):
    """Custom list class that extends the built-in list.
    
    This class includes an additional method to print the list in sorted order.
    """
    
    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
