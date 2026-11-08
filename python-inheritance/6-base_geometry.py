#!/usr/bin/python3
"""Module that defines the class BaseGeometry with an area method."""


class BaseGeometry:
    """Defines a base geometry."""

    def area(self):
        """Raise an Exception: area() must be implemented by subclasses."""
        raise Exception("area() is not implemented")
