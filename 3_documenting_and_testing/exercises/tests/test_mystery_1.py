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
    """test for addition of two items function"""
    
    def test1_add_positive_numbers(self):
        """Test addition of positive numbers"""
        self.assertEqual(mystery_1(4, 5), 9)

    def test2_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(mystery_1(-5, -6), -11)

    def test3_add_opposite_numbers(self):
        """Test addition of a positive and a negative number."""
        self.assertEqual(mystery_1(5, -3), 2)
        self.assertEqual(mystery_1(-3, 8), 5)

    def test4_add_floats(self):
        """Test addition of two float numbers."""
        self.assertAlmostEqual(mystery_1(1.5, 5.2), 6.7)
        
    def test5_add_with_zero(self):
        """Test addition of a number with zero"""
        self.assertEqual(mystery_1(0, 5), 5)
        self.assertEqual(mystery_1(5, 0), 5)


    def test6_concat_strings(self):
        """Test concatenation of two strings."""
        self.assertEqual(mystery_1("Safia", "Nouman"), "SafiaNouman")
