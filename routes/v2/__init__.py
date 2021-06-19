from fastapi import Request, Query
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from slowapi import Limiter
from slowapi.util import get_remote_address
from .. import cache
from interface import RestoreFirmware, OTAFirmware

from typing import List

limiter = Limiter(key_func=get_remote_address)
router = InferringRouter()


@cbv(router)
class LoyalRouterV2:
    @router.get("/restore", tags=["restore"], response_model=List[RestoreFirmware])
    @limiter.limit("240/minute")
    async def restore(
        self,
        request: Request,
        device: str = Query(
            None, description="iDevice's Identifier", example="iPhone12,1"
        ),
    ):
        return await cache.get(device, firm_type="Restore")

    @router.get("/ota", tags=["ota"], response_model=List[OTAFirmware])
    @limiter.limit("240/minute")
    async def ota(
        self,
        request: Request,
        device: str = Query(
            None, description="iDevice's Identifier", example="iPhone12,1"
        ),
    ):
        return await cache.get(device, firm_type="OTA")
