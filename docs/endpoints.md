# Endpoints

## v1

### `GET` /v1/restore

* Required Parameter: device (string, the identifier of iDevice)

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
    ...
```