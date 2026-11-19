#!/usr/bin/python3
"""Unittests for the class Rectangle."""
import contextlib
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


def captured(func):
    """Return what func prints to stdout."""
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        func()
    return out.getvalue()


class TestRectangle(unittest.TestCase):
    """Test cases for the class Rectangle."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Rectangle inherits from Base."""
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_init_defaults(self):
        """Default x, y and generated ids."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual((r1.width, r1.height, r1.x, r1.y), (10, 2, 0, 0))
        self.assertEqual((r1.id, r2.id), (1, 2))

    def test_init_all_args(self):
        """All the arguments are assigned."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5))

    def test_init_given_id(self):
        """A given id is kept."""
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_missing_args(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """At most 5 arguments are accepted."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_attributes(self):
        """The attributes are private."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)
        self.assertEqual(r._Rectangle__x, 3)
        self.assertEqual(r._Rectangle__y, 4)

    def test_setters(self):
        """The setters change the attributes."""
        r = Rectangle(1, 2)
        r.width, r.height, r.x, r.y = 5, 6, 7, 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_type_errors(self):
        """A non integer value raises TypeError."""
        bad = ["2", 2.5, None, {}, [1], (1,), True, {1}]
        for name in ("width", "height", "x", "y"):
            for value in bad:
                with self.subTest(name=name, value=value):
                    r = Rectangle(1, 1)
                    with self.assertRaises(TypeError) as ctx:
                        setattr(r, name, value)
                    self.assertEqual(str(ctx.exception),
                                     name + " must be an integer")

    def test_type_errors_init(self):
        """TypeError messages when instantiating."""
        cases = [((10, "2"), "height"), (("a", 2), "width"),
                 ((1, 2, {}), "x"), ((1, 2, 3, "4"), "y")]
        for args, name in cases:
            with self.subTest(args=args):
                with self.assertRaises(TypeError) as ctx:
                    Rectangle(*args)
                self.assertEqual(str(ctx.exception),
                                 name + " must be an integer")

    def test_width_height_positive(self):
        """Width and height must be > 0."""
        for name in ("width", "height"):
            for value in (0, -1, -10):
                with self.subTest(name=name, value=value):
                    r = Rectangle(1, 1)
                    with self.assertRaises(ValueError) as ctx:
                        setattr(r, name, value)
                    self.assertEqual(str(ctx.exception),
                                     name + " must be > 0")

    def test_x_y_not_negative(self):
        """X and y must be >= 0."""
        for name in ("x", "y"):
            with self.subTest(name=name):
                r = Rectangle(1, 1)
                with self.assertRaises(ValueError) as ctx:
                    setattr(r, name, -1)
                self.assertEqual(str(ctx.exception),
                                 name + " must be >= 0")
                setattr(r, name, 0)
                self.assertEqual(getattr(r, name), 0)

    def test_value_errors_init(self):
        """ValueError messages when instantiating."""
        cases = [((0, 1), "width must be > 0"),
                 ((1, -2), "height must be > 0"),
                 ((1, 2, -3), "x must be >= 0"),
                 ((10, 2, 3, -1), "y must be >= 0")]
        for args, msg in cases:
            with self.subTest(args=args):
                with self.assertRaises(ValueError) as ctx:
                    Rectangle(*args)
                self.assertEqual(str(ctx.exception), msg)

    def test_validation_order(self):
        """Width is validated before height."""
        with self.assertRaises(TypeError) as ctx:
            Rectangle("a", "b")
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_area(self):
        """Area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_after_change(self):
        """Area follows attribute changes."""
        r = Rectangle(2, 3)
        r.width = 10
        self.assertEqual(r.area(), 30)

    def test_display_no_offset(self):
        """Display without x and y."""
        self.assertEqual(captured(Rectangle(4, 2).display),
                         "####\n####\n")
        self.assertEqual(captured(Rectangle(1, 1).display), "#\n")

    def test_display_offsets(self):
        """Display with x and y."""
        self.assertEqual(captured(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(captured(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_str(self):
        """String representation."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_print_uses_str(self):
        """Print displays the string representation."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(captured(lambda: print(r)),
                         "[Rectangle] (5) 3/4 - 1/2\n")

    def test_update_args(self):
        """Update with no keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args(self):
        """Extra positional arguments are ignored."""
        r = Rectangle(1, 1)
        r.update(5, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (5) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_win(self):
        """Keyword arguments are skipped when args exist."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(5, width=99)
        self.assertEqual(str(r), "[Rectangle] (5) 10/10 - 10/10")

    def test_update_unknown_kwarg(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(color="red")
        self.assertFalse(hasattr(r, "color"))
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_no_arg(self):
        """Update without arguments changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_validates(self):
        """Update uses the validation of the setters."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(width=-4)

    def test_to_dictionary(self):
        """Dictionary representation."""
        r = Rectangle(10, 2, 1, 9, 7)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 7, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """A dictionary can update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_is_copy(self):
        """Changing the dictionary does not change the rectangle."""
        r = Rectangle(1, 2)
        r.to_dictionary()["width"] = 50
        self.assertEqual(r.width, 1)


if __name__ == "__main__":
    unittest.main()
