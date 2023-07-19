#!/usr/bin/env python3
"""ALX SE"""
import redis
import uuid
from typing import Any


class Cache:
    """Interact with the redis db"""
    def __init__(self):
        """store an instance of the Redis client and flush the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """
        generates a random key and store the store the input data in Redis
        using the random key, returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
