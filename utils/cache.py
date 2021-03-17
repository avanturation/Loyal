import asyncio
from contextlib import suppress

from .device import *
from .model import *
from .request import HTTP


class Cache:
    def __init__(self) -> None:
        self.restore_cache = {}
        self.ota_cache = {}

    async def fetch_restore(self):
        restore_cache = {}
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

        for plist in raw_plist:
            raw_data = plist["MobileDeviceSoftwareVersionsByVersion"]
            for index in raw_data:
                device_list = raw_data[index]["MobileDeviceSoftwareVersions"]

                for device in device_list:
                    firmware_list = device_list[device]

                    for builds in firmware_list:
                        if (
                            not builds == "Unknown"
                            and "Restore" in firmware_list[builds]
                        ):
                            firmware = firmware_list[builds]["Restore"]
                            if not device in restore_cache:
                                restore_cache[device] = []

                            restore_cache[device].append(
                                RestoreFirmware(
                                    build_id=None
                                    if not "BuildVersion" in firmware
                                    else firmware["BuildVersion"],
                                    docs_url=None
                                    if not "DocumentationURL" in firmware
                                    else firmware["DocumentationURL"],
                                    sha1=None
                                    if not "FirmwareSHA1" in firmware
                                    else firmware["FirmwareSHA1"],
                                    url=None
                                    if not "FirmwareURL" in firmware
                                    else firmware["FirmwareURL"],
                                    version=None
                                    if not "ProductVersion" in firmware
                                    else firmware["ProductVersion"],
                                )
                            )

        self.restore_cache = restore_cache
        print("restore caching finished")

    def build_ota_url(self):
        audio_url = [
            f"/com_apple_MobileAsset_MobileAccessoryUpdate_{airpods}_EA/com_apple_MobileAsset_MobileAccessoryUpdate_{airpods}_EA.xml"
            for airpods in AudioDevices
        ]
        accessory_url = [
            f"/com.apple.MobileAsset.MobileAccessoryUpdate.{accessory}/com.apple.MobileAsset.MobileAccessoryUpdate.{accessory}.xml"
            for accessory in Accesories
        ]

        return audio_url + accessory_url

    def check_type(self, asset_type: str):
        if "MobileAccessoryUpdate" in asset_type:  # Audio or Accessory
            if asset_type.split(".")[-1] == "EA":  # AirPdos, Beats
                return asset_type.split(".")[-2]

            return asset_type.replace(  # Apple Pencil, Folio Keyboard
                "com.apple.MobileAsset.MobileAccessoryUpdate.", ""
            )

        return "Regular"  # iPhone, HomePods, Apple Watch, Apple TV

    async def fetch_ota(self):
        ota_cache = {}
        device_urls = self.build_ota_url() + [
            TVOSXML,
            iOSXML,
            AudioOSXML,
            WatchOSXML,
        ]  # gather Apple XMLs
        raw_plists = [
            await HTTP.send_request("mesu", asset=asset)
            for asset in device_urls  # sending request
        ]

        for plist in raw_plists:
            device_type = "Regular"

            with suppress(Exception):
                if "AssetType" in plist:
                    device_type = self.check_type(
                        plist["AssetType"]
                    )  # discriminate device type

                for raw in plist["Assets"]:
                    firmware_dict = raw

                    ota_data = OTAFirmware(
                        version=None
                        if not "OSVersion" in firmware_dict
                        else firmware_dict["OSVersion"],
                        url=None
                        if not "__RelativePath" in firmware_dict
                        else firmware_dict["__BaseURL"]
                        + firmware_dict["__RelativePath"],
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

    async def get(self, device: str, type: str):
        if type == "Restore":
            return self.restore_cache[device]

        return self.ota_cache[device]

    async def cache(self, second: float):
        while True:
            await self.fetch_restore()
            await self.fetch_ota()

            await asyncio.sleep(second)
