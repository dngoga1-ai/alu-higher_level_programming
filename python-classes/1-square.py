#!/usr/bin/python3
"""Module that defines a Square with a private size."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """Initialize a square with a size (no validation)."""
        self.__size = size
