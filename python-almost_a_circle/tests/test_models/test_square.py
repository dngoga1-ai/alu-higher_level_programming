#!/usr/bin/python3
"""Unittests for the class Square."""
import contextlib
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def captured(func):
    """Return what func prints to stdout."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        func()
    return out.getvalue()


class TestSquare(unittest.TestCase):
    """Test cases for the class Square."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Square inherits from Rectangle and Base."""
        s = Square(1)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_init(self):
        """Attributes and default values."""
        s = Square(5)
        self.assertEqual((s.size, s.width, s.height), (5, 5, 5))
        self.assertEqual((s.x, s.y, s.id), (0, 0, 1))

    def test_init_all_args(self):
        """All the arguments are assigned."""
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 2, 3, 4))

    def test_ids(self):
        """Ids are shared with the other classes."""
        a = Square(1)
        b = Rectangle(1, 1)
        c = Square(1)
        self.assertEqual((a.id, b.id, c.id), (1, 2, 3))

    def test_missing_args(self):
        """Size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """At most 4 arguments are accepted."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_type_errors(self):
        """Non integer values raise TypeError."""
        for value in ("1", 1.5, None, [1], {}, (1,), True):
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as ctx:
                    Square(value)
                self.assertEqual(str(ctx.exception),
                                 "width must be an integer")

    def test_type_errors_x_y(self):
        """Non integer x or y raise TypeError."""
        with self.assertRaises(TypeError) as ctx:
            Square(1, "2")
        self.assertEqual(str(ctx.exception), "x must be an integer")
        with self.assertRaises(TypeError) as ctx:
            Square(1, 2, {})
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_value_errors(self):
        """Invalid values raise ValueError."""
        with self.assertRaises(ValueError) as ctx:
            Square(0)
        self.assertEqual(str(ctx.exception), "width must be > 0")
        with self.assertRaises(ValueError) as ctx:
            Square(-3)
        self.assertEqual(str(ctx.exception), "width must be > 0")
        with self.assertRaises(ValueError) as ctx:
            Square(1, -1)
        self.assertEqual(str(ctx.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as ctx:
            Square(1, 1, -1)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_area(self):
        """Area is size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        """Display with x and y."""
        self.assertEqual(captured(Square(2).display), "##\n##\n")
        self.assertEqual(captured(Square(2, 2).display), "  ##\n  ##\n")
        self.assertEqual(captured(Square(2, 1, 3).display),
                         "\n\n\n ##\n ##\n")

    def test_str(self):
        """String representation."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3, 9)), "[Square] (9) 1/3 - 3")

    def test_size_getter_setter(self):
        """Size sets the width and the height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_validation(self):
        """The size setter validates its value."""
        s = Square(5)
        with self.assertRaises(TypeError) as ctx:
            s.size = "9"
        self.assertEqual(str(ctx.exception), "width must be an integer")
        with self.assertRaises(ValueError) as ctx:
            s.size = 0
        self.assertEqual(str(ctx.exception), "width must be > 0")
        self.assertEqual(s.size, 5)

    def test_update_args(self):
        """Update with no keyword arguments."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_extra_args(self):
        """Extra positional arguments are ignored."""
        s = Square(5)
        s.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Update with keyword arguments."""
        s = Square(5, 0, 0, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_win(self):
        """Keyword arguments are skipped when args exist."""
        s = Square(5, 0, 0, 1)
        s.update(3, size=99)
        self.assertEqual(str(s), "[Square] (3) 0/0 - 5")

    def test_update_unknown_kwarg(self):
        """Unknown keys are ignored."""
        s = Square(1, 0, 0, 1)
        s.update(color="red", width=50)
        self.assertFalse(hasattr(s, "color"))
        self.assertEqual(s.size, 1)

    def test_update_validates(self):
        """Update uses the validation of the setters."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "a")
        with self.assertRaises(ValueError):
            s.update(size=-1)

    def test_to_dictionary(self):
        """Dictionary representation has id, size, x and y."""
        s = Square(10, 2, 1, 4)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 4, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_update(self):
        """A dictionary can update another square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_constructor_cases(self):
        """Valid and invalid ways of creating a Square."""
        self.assertEqual(Square(1).size, 1)
        self.assertEqual(Square(1, 2).x, 2)
        self.assertEqual(Square(1, 2, 3).y, 3)
        self.assertEqual(Square(1, 2, 3, 4).id, 4)
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_update_kwargs_progressive(self):
        """Update with a growing dictionary of attributes."""
        s = Square(5)
        s.update(**{'id': 89})
        s.update(**{'id': 89, 'size': 1})
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_progressive(self):
        """Create with a growing dictionary of attributes."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_args_progressive(self):
        """Update with a growing list of arguments."""
        s = Square(5)
        s.update(89)
        s.update(89, 1)
        s.update(89, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")


if __name__ == "__main__":
    unittest.main()
