#!/usr/bin/python3
"""Module that defines the function text_indentation.

The function prints a text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.

    There is no space at the beginning or at the end of printed lines.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(), end="\n\n")
            line = ""
    print(line.strip(), end="")
