#!/usr/bin/python3
"""Module that defines the function class_to_json."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON."""
    return obj.__dict__
