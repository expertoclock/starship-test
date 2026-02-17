"""Cache."""
from functools import lru_cache
@lru_cache(128)
def expensive(n): return sum(i*i for i in range(n))
