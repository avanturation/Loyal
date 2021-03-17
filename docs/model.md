# Models

## RestoreFirmware

* This class is dataclass.

| Arguments | Type | Description |
|-----------|------|-------------|
| build_id | str | Build ID of the firmware. |
| docs_url | str | Documentation URL of the firmware. |
| sha1 | str | SHA1 value of the firmware. |
| url | str | URL of the firmware file. |
| version | str | Version of the firmware. |

## OTAFirmware

* This class is dataclass.

| Arguments | Type | Description |
|-----------|------|-------------|
| build_id | str | Build ID of the firmware. |
| size | int | File size of the firmware. |
| product_name | str | OS name of the firmware. |
| release_type | str | Type of the firmware. (Beta or Release) |
| url | str | URL of the firmware file. |
| version | str | Version of the firmware. |
