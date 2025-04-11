#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square.
        
        Args:
            size (int): The size of the square (no type/value verification).
        """
        self.__size = size
