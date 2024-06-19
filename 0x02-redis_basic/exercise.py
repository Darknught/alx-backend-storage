#!/usr/bin/env python3
""" A Cache class that store an instance of the Redis client."""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """ Init method creates a new Redis client instance using redis.Redis()
        and stores it as a private variable and clears the entire Redis databas
        using flushdb()
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method takes a data arg and returns a string.
        It generates a random key using uuid and store the input data in Redis
        using the random key and return the key.
        """
        key = str(uuid.uuid4())
        if isinstance(data, str):
            self._redis.set(key, data.encode())
        else:
            self._redis.set(key, data)
        return key
