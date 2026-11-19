#!/usr/bin/python3
"""Module that defines the class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): x position of the rectangle.
            y (int): y position of the rectangle.
            id (int): identity of the rectangle.
        Raises:
            TypeError: if an attribute is not an integer.
            ValueError: if width or height is <= 0, or x or y is < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate(name, value, strict):
        """Validate an integer attribute.

        Args:
            name (str): name of the attribute, used in error messages.
            value: the value to validate.
            strict (bool): if True value must be > 0, else >= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if strict and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not strict and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self._validate("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self._validate("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x position of the rectangle."""
        self._validate("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y position of the rectangle."""
        self._validate("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, using x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from arguments.

        Args:
            *args: id, width, height, x and y, in this order.
            **kwargs: attributes by name, skipped if args is not empty.
        """
        if args:
            names = ["id", "width", "height", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
            return
        for name, value in kwargs.items():
            if name in ("id", "width", "height", "x", "y"):
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
