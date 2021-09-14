# Loyal

Fast, Simple API for fetching Apple Firmwares.

**The API server is closed due to some reasons. Wait for v2 releases."

## Features

* Fetching Signed IPSWs
* Fetching Signed OTAs
* Fetching not only iDevices but also AirPods, Beats, and Keyboard Accessories

### Example Request

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

## Documentation

You can read documentation on [here](./docs).

## Build and run

### Tested Environment

* [macOS Big Sur 11.1](https://www.apple.com/macos/big-sur/)

* [Python 3.8.6 for Darwin](https://www.python.org/downloads/release/python-386/)

* [MacBookPro15,1](https://support.apple.com/kb/SP776) and [Macmini9,1](https://www.apple.com/mac-mini/) (Tested on M1)


```bash
git clone https://github.com/fxrcha/Loyal

python3 -m pip install -r requirements.txt

python3 -m app
```

## Contributing

You can make pull requests or issues.
