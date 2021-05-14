#!/usr/bin/python3
"""Unittest for max_integer"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
"""Unittest for max_integer"""

    def test_one_negative_number(self):
        """Test a list of numbers including one negative"""
        one_neg_num = [2, 4, 24, -9, 255]
        self.assertEqual(max_integer(one_neg_num), 255)

    def test_only_negative_numbers(self):
        """Test a list of negative numbers"""
        neg_num = [-3, -56, -15, -99, -2.2, -3.5]
        self.assertEqual(max_integer(neg_num), -2.2)

    def test_one_element(self):
        """Test a list of one"""
        one_ele = [5]
        self.assertEqual(max_integer(one_ele), 5)

    def test_max_at_beginning(self):
        """Test a list of numbers """
        beg = [10, 8, 9, 5]
        self.assertEqual(max_integer(beg), 10)

    def test_max_in_the_middle(self):
        """Test a list of numbers"""
        mid = [5, 4, 15, 3, 1]
        self.assertEqual(max_integer(mid), 15)

    def test_max_end(self):
        """Test a list of numbers"""
        end = [1, 16, 7, 9, 23]
        self.assertEqual(max_integer(end), 23)

    def test_list_empty(self):
        """Test a list of numbers"""
        empty = []
        self.assertEqual(max_integer(empty), None)

