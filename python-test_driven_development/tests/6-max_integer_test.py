#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer."""

    def test_ordered_list(self):
        """Max of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning of the list."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        """Max in the middle of the list."""
        self.assertEqual(max_integer([1, 2, 99, 4, 5]), 99)

    def test_max_at_end(self):
        """Max at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def test_one_element(self):
        """List with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """No argument returns None."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """List of negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """List with positive and negative numbers."""
        self.assertEqual(max_integer([-3, 0, 5, -10]), 5)

    def test_duplicates(self):
        """List with repeated maximum values."""
        self.assertEqual(max_integer([4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 5, 5, 2]), 5)

    def test_floats(self):
        """List of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """List mixing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """List with very large numbers."""
        self.assertEqual(max_integer([10 ** 20, 5, 10 ** 19]), 10 ** 20)

    def test_strings(self):
        """List of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_string_argument(self):
        """A string is a sequence of characters."""
        self.assertEqual(max_integer("abc"), "c")

    def test_tuple_argument(self):
        """A tuple works like a list."""
        self.assertEqual(max_integer((1, 3, 2)), 3)

    def test_list_of_lists(self):
        """List of lists compares element by element."""
        self.assertEqual(max_integer([[1, 2], [1, 3]]), [1, 3])

    def test_mixed_types(self):
        """Comparing an integer and a string raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none_argument(self):
        """None has no length."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_argument(self):
        """An integer has no length."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
