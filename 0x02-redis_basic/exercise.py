#!/usr/bin/env python3
"""ALX SE"""
import redis
import uuid
from typing import Any, Callable, Union, Optional


class Cache:
    """Interact with the redis db"""
    def __init__(self) -> None:
        """store an instance of the Redis client and flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random key and store the store the input data in Redis
        using the random key, returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        converts redis return value type into the correct type
        """
        value = self._redis.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_int(self, data: bytes) -> int:
        """converts the type from bytes to int"""
        return int(data)

    def get_str(self, data: bytes) -> str:
        """converts the type from bytes to int"""
        return data.decode('utf-8')

