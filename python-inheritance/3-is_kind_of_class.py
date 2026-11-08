#!/usr/bin/python3
"""Module that defines the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass."""
    return isinstance(obj, a_class)
