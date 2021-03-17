from dataclasses import dataclass
from typing import List, Optional


@dataclass
class RestoreFirmware:
    build_id: str
    docs_url: Optional[str]
    sha1: str
    url: str
    version: str


@dataclass
class OTAFirmware:
    version: Optional[str]
    url: Optional[str]
    build_id: Optional[str]
    product_name: Optional[str]
    release_type: Optional[str]
    size: Optional[int]
