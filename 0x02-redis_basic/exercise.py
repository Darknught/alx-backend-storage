#!/usr/bin/env python3
""" A Cache class that store an instance of the Redis client."""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(
            self, key: str, fn: Optional[Callable[[bytes], Union[
                str, int, float]]] = None) -> Optional[Union[str, int, float]]:
        """
        Retrieves the data stored under the given key from the Redis cache.

        Args:
            key (str): The key of the data to be retrieved.
            fn (Optional[Callable[[bytes], Union[str, int, float]]]):
            An optional function to convert the retrieved data to the
            desired format.

        Returns:
            Optional[Union[str, int, float]]: The retrieved data, converted
            using the provided function if specified,
            or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value.decode()
        else:
            return fn(value)

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves the data stored under the given key as a string.

        Args:
            key (str): The key of the data to be retrieved.

        Returns:
            Optional[str]: The retrieved data as a string,
            or None if the key does not exist.
        """
        return self.get(key, lambda x: x.decode())

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves the data stored under the given key as an integer.

        Args:
            key (str): The key of the data to be retrieved.

        Returns:
            Optional[int]: The retrieved data as an integer,
            or None if the key does not exist.
        """
        return self.get(key, lambda x: int(x.decode()))
