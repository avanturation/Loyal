from fastapi import Request
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from slowapi import Limiter
from slowapi.util import get_remote_address
from .. import cache

limiter = Limiter(key_func=get_remote_address)
router = InferringRouter()


@cbv(router)
class LoyalRouterV1:
    @router.get("/restore")
    @limiter.limit("240/minute")
    async def restore(self, device: str, request: Request):
        return await cache.get(device, firm_type="Restore")

    @router.get("/ota")
    @limiter.limit("240/minute")
    async def ota(self, device: str, request: Request):
        return await cache.get(device, firm_type="OTA")
