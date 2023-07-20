#!/usr/bin/env python3

"""
Exercise File

File bears the Cache class
"""

import redis
import uuid
from typing import Callable, Union


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Fetches data from Redis based on a key

        Args:
        key (str) - Redis key whose value is to be retrieved
        fn - conversion function to convert data to desired type

        Return:
        value - data associated with key, otherwise None
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            data = fn(data)

        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Fetches the data from Redis based on a key as a string

        Args:
        key (str) - Redis key whose value is to be retrieved

        Return:
        value - string representation of data associated with key
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[int, None]:
        """
        Fetches the data from Redis based on a key as an int

        Args:
        key (str) - Redis key whose value is to be retrieved

        Return:
        value - int representation of data associated with key
        """
        return self.get(key, int)
