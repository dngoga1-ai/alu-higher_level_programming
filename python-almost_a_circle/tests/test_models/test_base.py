#!/usr/bin/python3
"""Unittests for the class Base."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the class Base."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove the JSON files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_is_class(self):
        """Base is a class and its instances are Base."""
        self.assertIsInstance(Base(), Base)

    def test_auto_ids(self):
        """Ids are generated one after another."""
        self.assertEqual([Base().id for _ in range(3)], [1, 2, 3])

    def test_given_id(self):
        """A given id is used and does not touch the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_mixed_ids(self):
        """Given ids and generated ids can be mixed."""
        ids = [Base().id, Base().id, Base(12).id, Base().id]
        self.assertEqual(ids, [1, 2, 12, 3])

    def test_zero_and_negative_id(self):
        """Falsy and negative ids are kept as given."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)

    def test_id_other_types(self):
        """Any non None id is kept without validation."""
        self.assertEqual(Base("abc").id, "abc")
        self.assertEqual(Base([1]).id, [1])

    def test_id_is_public(self):
        """The id attribute can be changed."""
        b = Base()
        b.id = 99
        self.assertEqual(b.id, 99)

    def test_nb_objects_private(self):
        """The counter is private."""
        self.assertFalse(hasattr(Base, "__nb_objects"))
        self.assertEqual(Base._Base__nb_objects, 0)
        Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_too_many_args(self):
        """Base takes at most one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_none(self):
        """None gives an empty JSON list."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list gives an empty JSON list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """A list of dictionaries gives a JSON string."""
        s = Base.to_json_string([{"id": 1, "width": 2}])
        self.assertIsInstance(s, str)
        self.assertEqual(s, '[{"id": 1, "width": 2}]')

    def test_to_json_string_two_dicts(self):
        """Several dictionaries are all serialized."""
        s = Base.to_json_string([{"a": 1}, {"b": 2}])
        self.assertEqual(s, '[{"a": 1}, {"b": 2}]')

    def test_to_json_string_no_arg(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """A JSON list gives a list of dictionaries."""
        out = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertIsInstance(out, list)
        self.assertEqual(out, [{"id": 89, "width": 10}])

    def test_json_round_trip(self):
        """to_json_string and from_json_string are inverse."""
        data = [{"id": 1, "x": 2}, {"id": 3, "x": 4}]
        out = Base.from_json_string(Base.to_json_string(data))
        self.assertEqual(out, data)

    def test_from_json_string_no_arg(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_save_rectangles(self):
        """Rectangles are saved in Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """Squares are saved in Square.json."""
        s1 = Square(5, 1, 2, 7)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [s1.to_dictionary()])

    def test_save_none(self):
        """None is saved as an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        """An empty list is saved as an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_base(self):
        """Base can save an empty list in Base.json."""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites(self):
        """An existing file is overwritten."""
        Rectangle.save_to_file([Rectangle(1, 1), Rectangle(2, 2)])
        Rectangle.save_to_file([Rectangle(3, 3, 0, 0, 50)])
        with open("Rectangle.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["id"], 50)

    def test_save_no_arg(self):
        """The argument is required."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_create_rectangle(self):
        """create builds a Rectangle with all attributes set."""
        r1 = Rectangle(3, 5, 1, 2, 9)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """create builds a Square with all attributes set."""
        s1 = Square(4, 1, 2, 9)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_create_partial(self):
        """create works with a partial dictionary."""
        r = Rectangle.create(id=5, width=7, height=8)
        self.assertEqual(str(r), "[Rectangle] (5) 0/0 - 7/8")

    def test_load_no_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """Rectangles are loaded as new instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertTrue(all(isinstance(r, Rectangle) for r in out))
        self.assertEqual([str(r) for r in out], [str(r1), str(r2)])
        self.assertIsNot(out[0], r1)

    def test_load_squares(self):
        """Squares are loaded as Square instances."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertTrue(all(isinstance(s, Square) for s in out))
        self.assertEqual([str(s) for s in out], [str(s1), str(s2)])

    def test_load_empty_file(self):
        """A file with an empty list gives an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])


    def test_square_save_to_file_none(self):
        """Square.save_to_file(None) saves an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_square(self):
        """Square.save_to_file([Square(1)]) saves one square."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["size"], 1)

    def test_rectangle_save_to_file_rectangle(self):
        """Rectangle.save_to_file([Rectangle(1, 2)]) saves one rectangle."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["width"], 1)

    def test_base_exact_cases(self):
        """The basic examples of Base."""
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'),
                         [{"id": 89}])


if __name__ == "__main__":
    unittest.main()
