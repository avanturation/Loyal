from utils.cache import Cache

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()
cache = Cache()


@cbv(router)
class LoyalRouter:
    @router.get("/restore")
    async def restore(self, device: str):
        return await cache.get(device, firm_type="Restore")

    @router.get("/ota")
    async def ota(self, device: str):
        return await cache.get(device, firm_type="OTA")