# Endpoints

## v1

### `GET` /v1/restore

* Required Parameter: device (string, the identifier of iDevice)

* Returns: List(RestoreFirmware)

#### Example Response

```bash
curl -X GET "loyalapi.ml/v1/restore?device=iPhone12,1"
```

```json
[
    {
        "build_id": "18D61",
        "docs_url": "http://updates-http.cdn-apple.com/2021WinterFCS/documentation/071-15446/2D646674-5AE5-454D-94C9-EBA3E76437D7/iPhoneiTunesUpdateReadMe.ipd",
        "sha1": "45186bb240128a11a26a2342a6efeb87cfd1c029",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/fullrestores/071-12530/598B4392-EF03-4F6C-962A-3A8CC9BA9DAC/iPhone11,8,iPhone12,1_14.4.1_18D61_Restore.ipsw",
        "version": "14.4.1"
    },
    {
        "build_id": "18D61",
        "docs_url": "http://updates-http.cdn-apple.com/2021WinterFCS/documentation/071-15446/2D646674-5AE5-454D-94C9-EBA3E76437D7/iPhoneiTunesUpdateReadMe.ipd",
        "sha1": "45186bb240128a11a26a2342a6efeb87cfd1c029",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/fullrestores/071-12530/598B4392-EF03-4F6C-962A-3A8CC9BA9DAC/iPhone11,8,iPhone12,1_14.4.1_18D61_Restore.ipsw",
        "version": "14.4.1"
    }
]
```

### `GET` /v1/ota

* Required Parameter: device (string, the identifier of device)

If you are going to get AirPods / Accessories firmware, you **must put these values into parameter**.

* Returns: List(OTAFirmware)

#### AirPods

| Parameter | Device |
|-----------|--------|
| `A1523` | AirPods (1st generation) |
| `A2032` | AirPods (2nd generation) |
| `A2084` | AirPods Pro |
| `A2096` | AirPods Max |
| `A1796` | Beats Solo3 Wireless |
| `A1881` | Beats Solo Pro |
| `A1914` | Beats Studio 3 Wireless |
| `A1747` | Beats X |
| `A1763` | PowerBeats 3 | 
| `A2048` | PowerBeats Pro |
| `A2015` | PowerBeats |

#### Accessories

| Parameter | Device |
|-----------|--------|
| `WirelessStylusFirmware` | Apple Pencil (1st generation) |
| `WirelessStylusFirmware.2` | Apple Pencil (2nd generation) |
| `WirelessRemoteFirmware` | Siri Remote |
| `WirelessRemoteFirmware.2` | Siri Remote (2nd generation) |
| `KeyboardCoverFirmware` | Smart Keyboard |
| `KeyboardCoverFirmware.4` | Smart Keyboard Folio (11-inch) |
| `KeyboardCoverFirmware.5` | Smart Keyboard Folio (12.9-inch) |


#### Example Response

```bash
curl -X GET "loyalapi.ml/v1/ota?device=Watch5,4"
```

```json
[
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88622/6D5315EB-052F-43E8-B165-B6D76CB17F32/com_apple_MobileAsset_SoftwareUpdate/cb5d0e33da81485a3682c095dddc58701d8214ea.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 609853814
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88799/711FB89A-9F7C-4197-8EF7-B841820E35CB/com_apple_MobileAsset_SoftwareUpdate/cf24a3f8516e668589053eb1eda87e4bd570a625.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 609962832
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88714/D8733A34-A397-4E49-B7F6-FE86D4779C61/com_apple_MobileAsset_SoftwareUpdate/a9aecb55a809f0c2902b6eabd849092a12fef47a.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 470069334
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88808/01F0403D-F75D-4F4D-9C28-A63C37617FAD/com_apple_MobileAsset_SoftwareUpdate/98595e26a88deb34e752d46deef2a92578f072de.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 467662290
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88877/C753C993-29BA-4440-98B5-2FE8494B7726/com_apple_MobileAsset_SoftwareUpdate/c82ffc81851feaba75f0c127068dfa05dc7399b7.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 467663750
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88572/C5BCAABF-8BF3-417F-AECB-D43191577832/com_apple_MobileAsset_SoftwareUpdate/cf4b5e698e7dcdfd842f96b5b87dd0bd7bf58d6c.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 481733353
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88968/C8A452C7-4E1F-4E29-8DDC-7F996DE93A12/com_apple_MobileAsset_SoftwareUpdate/d818cd5c7badd311111965ec91cd7667f8a3fca9.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 198690038
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88675/7DEDCC95-CC60-4D08-8767-80E34122668D/com_apple_MobileAsset_SoftwareUpdate/45ee4793a04335a5e7941a6ce5ede894410a1185.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 198707229
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88900/A692CF0F-BFB2-4E24-B3C3-34B8A6AA4A12/com_apple_MobileAsset_SoftwareUpdate/748fd91151832c30402b2805a1b186390947a533.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 140034754
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88821/80DADA5F-DAA1-4878-B974-B03B6C7D4281/com_apple_MobileAsset_SoftwareUpdate/1420e706d66341c81d94228fa97a77482c2d6657.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 140021097
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-95823/D2824C42-6E07-4673-8510-E371277B9748/com_apple_MobileAsset_SoftwareUpdate/20fbdbf3dc5d8f2eb7f9179029fa3206d42cd49b.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 79763808
    },
    {
        "version": "6.3",
        "url": "http://updates-http.cdn-apple.com/2021WinterFCS/patches/001-88474/10F8653E-D128-4F8A-8B10-3C7DAC01AF5C/com_apple_MobileAsset_SoftwareUpdate/94df61e66b4af2fed7cc69089de0b7cbd82856e8.zip",
        "build_id": "17U216",
        "product_name": "iOS",
        "release_type": null,
        "size": 1521267994
    }
]
```