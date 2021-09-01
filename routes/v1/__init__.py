from fastapi import Request
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from slowapi import Limiter
from slowapi.util import get_remote_address
from utils.cache import cache

v1_limiter = Limiter(key_func=get_remote_address)
v1_router = InferringRouter()


@cbv(v1_router)
class LoyalRouterV1:
    @v1_router.get("/restore")
    @v1_limiter.limit("240/minute")
    async def restore(self, device: str, request: Request):
        return "v1 is now obsolete. Use v2 instead."

    @v1_router.get("/ota")
    @v1_limiter.limit("240/minute")
    async def ota(self, device: str, request: Request):
        return "v1 is now obsolete. Use v2 instead."
