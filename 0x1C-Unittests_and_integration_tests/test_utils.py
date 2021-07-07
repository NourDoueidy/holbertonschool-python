#!/usr/bin/env python3
''' test module '''

import unittest
import parametrized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    ''' nested map test '''
    
    @parametrized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        ''' test access nested mapp '''
        self.assertEqual(access_nested_map(nested_map, path), expected)
        
    def test_access_nested_map_exception(self, nested_map, path):
        ''' test exception'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
