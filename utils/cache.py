import asyncio
import datetime
from contextlib import suppress

from .device import TVOSXML, Accesories, AudioDevices, AudioOSXML, WatchOSXML, iOSXML
from .model import OTAFirmware, RestoreFirmware
from .request import HTTP


class Cache:
    def __init__(self) -> None:
        self.restore_cache = {}
        self.ota_cache = {}

    async def cache_ota(self):
        device_urls = self.build_ota_url() + [
            TVOSXML,
            iOSXML,
            AudioOSXML,
            WatchOSXML,
        ]

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

    async def cache_restore(self):
        raw_plist = [
            await HTTP.send_request("itunes"),
            await HTTP.send_request(
                "mesu",
                asset="/bridgeos/com_apple_bridgeOSIPSW/com_apple_bridgeOSIPSW.xml",
            ),
            await HTTP.send_request(
                "mesu", asset="/macos/com_apple_macOSIPSW/com_apple_macOSIPSW.xml"
            ),
        ]

        restore_cache = {}

        for plist in raw_plist:
            for index in plist["MobileDeviceSoftwareVersionsByVersion"]:
                for device in plist["MobileDeviceSoftwareVersionsByVersion"][index][
                    "MobileDeviceSoftwareVersions"
                ]:
                    for builds in plist["MobileDeviceSoftwareVersionsByVersion"][index][
                        "MobileDeviceSoftwareVersions"
                    ][device]:
                        if (
                            not builds == "Unknown"
                            and "Restore"
                            in plist["MobileDeviceSoftwareVersionsByVersion"][index][
                                "MobileDeviceSoftwareVersions"
                            ][device][builds]
                        ):
                            if not device in restore_cache:
                                restore_cache[device] = []

                            restore_cache[device].append(
                                RestoreFirmware(
                                    build_id=None
                                    if not "BuildVersion"
                                    in plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ]
                                    else plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ][
                                        "BuildVersion"
                                    ],
                                    docs_url=None
                                    if not "DocumentationURL"
                                    in plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ]
                                    else plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ][
                                        "DocumentationURL"
                                    ],
                                    sha1=None
                                    if not "FirmwareSHA1"
                                    in plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ]
                                    else plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ][
                                        "FirmwareSHA1"
                                    ],
                                    url=None
                                    if not "FirmwareURL"
                                    in plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ]
                                    else plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ][
                                        "FirmwareURL"
                                    ],
                                    version=None
                                    if not "ProductVersion"
                                    in plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ]
                                    else plist["MobileDeviceSoftwareVersionsByVersion"][
                                        index
                                    ]["MobileDeviceSoftwareVersions"][device][builds][
                                        "Restore"
                                    ][
                                        "ProductVersion"
                                    ],
                                )
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

    def check_type(self, asset_type: str):
        if "MobileAccessoryUpdate" in asset_type:  # Audio or Accessory
            if asset_type.split(".")[-1] == "EA":  # AirPods, Beats
                return asset_type.split(".")[-2]

            return asset_type.replace(  # Apple Pencil, Folio Keyboard
                "com.apple.MobileAsset.MobileAccessoryUpdate.", ""
            )

        return "Regular"  # iPhone, HomePods, Apple Watch, Apple TV

    async def get(self, device: str, firm_type: str):
        if firm_type == "Restore":
            return self.restore_cache[device]

        return self.ota_cache[device]

    async def cache(self, second: float):
        while True:
            asyncio.gather(self.cache_restore(), self.cache_ota())
            await asyncio.sleep(second)


cache = Cache()
