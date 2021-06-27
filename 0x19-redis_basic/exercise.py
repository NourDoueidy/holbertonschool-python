#!/usr/bin/env pyrhon3
"""Redis Exercise"""
import redid
import uuid4


class Cache:
    """Defines a class Cache"""

    def __init__(self):
        """Initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key and store the input data and return key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
