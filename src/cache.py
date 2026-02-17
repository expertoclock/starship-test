"""Simple caching."""
from functools import lru_cache
from time import time

class Cache:
    def __init__(self, ttl=300):
        self._data = {}
        self._ttl = ttl

    def get(self, key):
        if key in self._data:
            val, ts = self._data[key]
            if time() - ts < self._ttl:
                return val
        return None

    def set(self, key, val):
        self._data[key] = (val, time())

@lru_cache(maxsize=128)
def expensive(n: int) -> int:
    return sum(i * i for i in range(n))
