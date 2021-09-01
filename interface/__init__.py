from dataclasses import dataclass
from typing import Optional


@dataclass
class RestoreFirmware:
    buildversion: Optional[str]
    productversion: Optional[str]
    documentationurl: Optional[str]
    firmwareurl: Optional[str]
    firmwaresha1: Optional[str]


@dataclass
class OTAFirmware:
    version: Optional[str]
    url: Optional[str]
    build_id: Optional[str]
    product_name: Optional[str]
    release_type: Optional[str]
    size: Optional[int]
