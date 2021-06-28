#!/usr/bin/env python3
"""Redis Exercise"""
import redis
import uuid
from typing import Union


class Cache():
    """Defines a class Cache"""
    
    def __init__(self):
        """Initializer"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key and store the input data and return key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
