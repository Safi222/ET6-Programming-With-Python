#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX
Updated on XX XX XX
@editor: Safia Gibril
"""
import unittest


# --- imports & test class before documenting and testing ---

# from ..mystery_1 import mystery_1

# class TestMystery1(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """test a function that adds 2 items"""

    def test_positive_numbers(self):
        """Test with two positive int"""
        self.assertEqual(mystery_1(3, 7), 10)

    def test_negative_numbers(self):
        """Test with two negative int"""
        self.assertEqual(mystery_1(-4, -6), -10)

    def test_opposite_sign_numbers(self):
        """Test with one positive and one negative int"""
        self.assertEqual(mystery_1(-3, 8), 5)

    def test_floats(self):
        """Test with two floats"""
        self.assertEqual(mystery_1(4.5, 4.5), 9.0)

    def test_concat_strings(self):
        """Test with concatenation string inputs"""
        self.assertEqual(mystery_1("MIT", "talent"), "MITtalent")

    def test_empty_string_and_number(self):
        """Test with an empty string and a number."""
        self.assertEqual(mystery_1("", 5), "5")
