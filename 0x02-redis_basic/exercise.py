#!/usr/bin/env python3

"""
Exercise File

File bears the Cache class
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class

    Handles interactions with the Redis server
    """
    def __init__(self):
        """
        Constructs an instance of the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis using a random key

        Args:
        data - the data to be stored

        Return:
        value (str) - the key of the entry in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
