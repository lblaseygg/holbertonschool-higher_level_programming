#!/usr/bin/python3
"""This module provides a function to add two integers."""

def add_integer(a, b=98):
    """Adds two integers.
    
    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).
    
    Returns:
        The sum of a and b as an integer.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

