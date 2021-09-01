import asyncio
from typing import Dict, Tuple

from interface import OTAFirmware, RestoreFirmware

from .request import LoyalRequest

MDSVBV = "MobileDeviceSoftwareVersionsByVersion"
MDSV = "MobileDeviceSoftwareVersions"


class LoyalBackend:
    def __init__(self) -> None:
        self.restore_cache = {}
        self.ota_cache = {}

        self.HTTP = LoyalRequest()

        super().__init__()

    def __filter_keys(self, key) -> str:
        key = key.lower()
        key = key.replace("-", "_")
        return key

    def __lower_keys(self, data) -> Dict:
        return {self.__filter_keys(key): value for key, value in data.items()}

    async def cache_ota(self):
        device_urls = self.build_ota_url()
        raw_plists = [
            await HTTP.send_request("mesu", asset=asset) for asset in device_urls
        ]

        ota_cache = {}

        for plist in raw_plists:
            device_type = "Regular"

            if "AssetType" in plist:
                device_type = self.check_type(plist["AssetType"])

            for firmware_dict in plist["Assets"]:
                ota_data = OTAFirmware(
                    version=None
                    if not "OSVersion" in firmware_dict
                    else firmware_dict["OSVersion"],
                    url=None
                    if not "__RelativePath" in firmware_dict
                    else firmware_dict["__BaseURL"] + firmware_dict["__RelativePath"],
                    build_id=None
                    if not "Build" in firmware_dict
                    else firmware_dict["Build"],
                    product_name=None
                    if not "SUProductSystemName" in firmware_dict
                    else firmware_dict["SUProductSystemName"],
                    release_type=None
                    if not "ReleaseType" in firmware_dict
                    else firmware_dict["ReleaseType"],
                    size=None
                    if not "_DownloadSize" in firmware_dict
                    else firmware_dict["_DownloadSize"],
                )

                if device_type == "Regular":
                    for device in firmware_dict["SupportedDevices"]:
                        if not device in ota_cache:
                            ota_cache[device] = []

                        ota_cache[device].append(ota_data)

                else:
                    if not device_type in ota_cache:
                        ota_cache[device_type] = []

                    ota_cache[device_type].append(ota_data)

        self.ota_cache = ota_cache

    async def cache_restore(self, plist: Dict):
        restore_cache = {}

        for v in plist[MDSVBV].values():
            for idevice in v.values():
                for identifier, builds in idevice.items():
                    for build, firmware in builds.items():

                        if "SameAs" in firmware.keys():
                            restore_cache[identifier][build] = restore_cache[
                                identifier
                            ][firmware["SameAs"]]

                        if "Restore" in firmware.keys():
                            restore_cache[identifier][build] = RestoreFirmware(
                                **self.__lower_keys(firmware["Restore"])
                            )

        self.restore_cache = restore_cache

    def build_ota_url(self):
        audio_url = [
            f"/com_apple_MobileAsset_MobileAccessoryUpdate_{airpods}_EA" * 2 + ".xml"
            for airpods in AudioDevices
        ]
        accessory_url = [
            f"/com_apple_MobileAsset_MobileAccessoryUpdate_{accessory}" * 2 + ".xml"
            for accessory in Accesories
        ]

        return audio_url + accessory_url

    def create_beta_url(self, min: int, max: int) -> Tuple:
        developer_seed, public_seed = [], []

        for version in range(min, max + 1):
            developer_seed.append(iOSDeveloperXML.replace("<version>", version))
            public_seed.append(iOSPublicXML.replace("<version>", version))

        return (developer_seed, public_seed)

    def check_type(self, asset_type: str):
        if "MobileAccessoryUpdate" in asset_type:  # Audio or Accessory
            if asset_type.split(".")[-1] == "EA":  # AirPods, Beats
                return asset_type.split(".")[-2]

            return asset_type.replace(  # Apple Pencil, Folio Keyboard
                "com.apple.MobileAsset.MobileAccessoryUpdate.", ""
            )

        return "Regular"  # iPhone, HomePods, Apple Watch, Apple TV

    async def cache(self, second: float):
        while True:
            asyncio.gather(self.cache_restore(), self.cache_ota())
            await asyncio.sleep(second)


cache = Cache()
