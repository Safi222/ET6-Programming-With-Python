import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ """
import unittest

class TestMystery2(unittest.TestCase):
    """test for a function that returns a length of an string or none"""

    def test1_empty_string(self):
        """Test with an empty string."""
        self.assertIsNone(mystery_2(""))

    def test2_non_empty_string(self):
        """Test with a non-empty string."""
        self.assertEqual(mystery_2("hello"), 5)

    def test3_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(mystery_2([]))

    def test4_non_empty_list(self):
        """Test with a non-empty list."""
        self.assertEqual(mystery_2([1, 2, 3]), 3)

    def test5_tuple(self):
        """Test with a tuple."""
        self.assertEqual(mystery_2((6, 8)), 2)

    def test_list_of_lists(self):
        """Test with a list of lists"""
        self.assertEqual(mystery_2([[5, 6], [9, 4], [6, 7]]), 3)

    def test_string_with_spaces(self):
        """Test with a string with spaces and mixed characters"""
        self.assertEqual(mystery_2("Hi  ,Iam Okay!"), 15)
