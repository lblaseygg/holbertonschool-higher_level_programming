#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
    obj: The object to check.
    a_class: The class to compare the object against.

    Returns:
    True if the object is exactly an instance of the specified class.
    False otherwise.
    """
    return type(obj) is a_class
