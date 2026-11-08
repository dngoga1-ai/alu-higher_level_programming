#!/usr/bin/python3
"""Module that defines the function write_file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file (overwriting it).

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
