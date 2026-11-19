#!/usr/bin/python3
"""Module that defines the class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square, a rectangle with the same width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): size of the square.
            x (int): x position of the square.
            y (int): y position of the square.
            id (int): identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (width and height)."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assign attributes from arguments.

        Args:
            *args: id, size, x and y, in this order.
            **kwargs: attributes by name, skipped if args is not empty.
        """
        if args:
            names = ["id", "size", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
            return
        for name, value in kwargs.items():
            if name in ("id", "size", "x", "y"):
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
