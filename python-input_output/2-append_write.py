#!/usr/bin/python3
"""Module that defines the function append_write."""


def append_write(filename="", text=""):
    """Append text at the end of a UTF8 file (created if missing).

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
