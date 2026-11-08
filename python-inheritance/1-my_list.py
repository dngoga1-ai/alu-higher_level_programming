#!/usr/bin/python3
"""Module that defines the class MyList."""


class MyList(list):
    """A list with a method that prints itself sorted."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
