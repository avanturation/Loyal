import plistlib

import aiohttp

MESU_APPLE = "https://mesu.apple.com/assets"
ITUNES_SERVER = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/com.apple.jingle.appserver.client.MZITunesClientCheck/version"


class HTTP:
    @classmethod
    async def itunes_apple(cls):
        async with aiohttp.ClientSession() as session:
            async with session.get(ITUNES_SERVER) as resp:
                data = await resp.text(encoding="utf-8")
                return plistlib.loads(bytes(data, encoding="utf-8"))

    @classmethod
    async def mesu_apple(cls, asset: str):
        url = MESU_APPLE + asset
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.text(encoding="utf-8")
                return plistlib.loads(bytes(data, encoding="utf-8"))

    @classmethod
    async def send_request(cls, dest: str, **kwargs):
        if dest == "mesu":
            return await cls.mesu_apple(**kwargs)

        elif dest == "itunes":
            return await cls.itunes_apple()
