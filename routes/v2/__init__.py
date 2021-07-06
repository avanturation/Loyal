from fastapi import Request, Query
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from slowapi import Limiter
from slowapi.util import get_remote_address
from utils.cache import cache
from interface import RestoreFirmware, OTAFirmware

from typing import List

v2_limiter = Limiter(key_func=get_remote_address)
v2_router = InferringRouter()


@cbv(v2_router)
class LoyalRouterV2:
    @v2_router.get("/restore", tags=["restore"], response_model=List[RestoreFirmware])
    @v2_limiter.limit("240/minute")
    async def restore(
        self,
        request: Request,
        device: str = Query(
            None, description="iDevice's Identifier", example="iPhone12,1"
        ),
    ):
        return await cache.get(device, firm_type="Restore")

    @v2_router.get("/ota", tags=["ota"], response_model=List[OTAFirmware])
    @v2_limiter.limit("240/minute")
    async def ota(
        self,
        request: Request,
        device: str = Query(
            None, description="iDevice's Identifier", example="iPhone12,1"
        ),
    ):
        return await cache.get(device, firm_type="OTA")
