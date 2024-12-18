import unittest

from ..mystery_3 import mystery_3


class TestMystery3(unittest.TestCase):
    """test for a function that returns the max of two items if founded otherwise it adds them"""

    def test1_a_less_than_b(self):
        """Test the first number is lesser than the second"""
        self.assertEqual(mystery_3(4, 8), 4)

    def test2_a_greater_than_b(self):
        """Test the first number is greater than the second"""
        self.assertEqual(mystery_3(10, 7), 7)

    def test3_a_equal_to_b(self):
        """Test when two numbers are equal"""
        self.assertEqual(mystery_3(5, 5), 10)

    def test4_negative_numbers(self):
        """Test with two negative numbers."""
        self.assertEqual(mystery_3(-4, -7), -7)

    def test5_mixed_sign_numbers(self):
        """Test with one positive and one negative number"""
        self.assertEqual(mystery_3(-5, 3), -5)

    def test6_zero_and_positive(self):
        """Test when one number is zero and the other is positive."""
        self.assertEqual(mystery_3(0, 5), 0)

    def test7_zero_and_negative(self):
        """Test when one number is zero and the other is negative"""
        self.assertEqual(mystery_3(0, -4), -4)

    def test8_floats(self):
        """Test with float inputs."""
        self.assertEqual(mystery_3(3.2, 3.5), 3.2)

    def test9_large_numbers(self):
        """Test with very large numbers."""
        self.assertEqual(mystery_3(1200000, 1500000), 1200000)

    def test10_strings(self):
        """Test with string inputs."""
        self.assertEqual(mystery_3("iphone", "ipad"), "ipad")
