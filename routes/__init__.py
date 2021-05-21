from .v1 import limiter, router
from utils.cache import Cache

cache = Cache()

__all__ = ["router", "cache", "limiter"]
