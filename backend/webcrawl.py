from bs4 import BeautifulSoup
from typing import Dict, Literal

from aiohttp import ClientSession, TCPConnector

from request import LoyalRequest


class WikiCrawl:
    def __init__(self) -> None:
        self.HTTP = LoyalRequest()

        super().__init__()
