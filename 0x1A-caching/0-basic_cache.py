#!/usr/bin/python3
"""Basic Dicionary"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Defines the class"""

    def put(self, key, item):
        """method"""
        if key and item:
             self.cache_data[key] = item

    def get(self, key):
        """method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
