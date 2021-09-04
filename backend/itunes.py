from request import LoyalRequest

from typing import Literal, Dict

from interface import OTAFirmware, RestoreFirmware


MDSVBV = "MobileDeviceSoftwareVersionsByVersion"


class AppleInternalHandler:
    def __init__(self) -> None:
        self.restore_cache = {}
        self.ota_cache = {}

        self.HTTP = LoyalRequest()

    def __filter_keys(self, key) -> str:
        key = key.lower()
        key = key.replace("-", "_")
        return key

    def __lower_keys(self, data) -> Dict:
        return {self.__filter_keys(key): value for key, value in data.items()}

    async def parse_ota(self, plist: Dict):
        ota_cache = {}

    async def parse_restore(self, plist: Dict):
        restore_cache = {}

        for v in plist[MDSVBV].values():
            for idevice in v.values():
                for identifier, builds in idevice.items():
                    for build, firmware in builds.items():
                        keys = firmware.keys()

                        if "SameAs" in keys:
                            restore_cache[identifier][build] = restore_cache[
                                identifier
                            ][firmware["SameAs"]]

                        if "Restore" in keys:
                            restore_cache[identifier][build] = RestoreFirmware(
                                **self.__lower_keys(firmware["Restore"])
                            )

        self.restore_cache = restore_cache
