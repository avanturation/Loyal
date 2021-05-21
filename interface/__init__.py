from dataclasses import dataclass
from typing import Optional


@dataclass
class RestoreFirmware:
    build_id: Optional[str]
    docs_url: Optional[str]
    sha1: Optional[str]
    url: Optional[str]
    version: Optional[str]


@dataclass
class OTAFirmware:
    version: Optional[str]
    url: Optional[str]
    build_id: Optional[str]
    product_name: Optional[str]
    release_type: Optional[str]
    size: Optional[int]
