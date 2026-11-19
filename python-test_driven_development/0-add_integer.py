#!/usr/bin/python3
"""0-add_integer module.

Defines a function that adds two integers.
It casts floats to integers before adding.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as an integer.

    a and b must be integers or floats, otherwise a TypeError is raised."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
