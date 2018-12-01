# Coding exercise

- Execution environment: Linux/macOS
- Programming Language: Python 2.7.x and above

## Instructions

Your task is to create two Python applications communicating with each other (high-level IPC) where application A monitors the changes to a file which contains surrounding Wireless APs in JSON format and informs application B which is responsible for displaying the change in format of:


- SSID’s SNR and/or channel value has changed from X to Y
- SSID is added to the list with SNR <SNR> and channel <CHANNEL>
- SSID is removed from the list.


```json
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 63,
      "channel": 11
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 1
    },
    {
      "ssid": "HisAP",
      "snr": 54,
      "channel": 6
    }
  ]
}
```

cat /tmp/access_points (after X seconds)

```json
{
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 82,
      "channel": 11
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 6
    },
    {
      "ssid": "HerAP",
      "snr": 71,
      "channel": 1
    }
  ]
}
```

Expected output:

- MyAP’s SNR has changed from 63 to 62
- YourAP’s channel has changed from 1 to 6
- HisAP is removed from the list
- HerAP is added to the list with SNR 71 and channel 1

## Notes

The assignment is not about creating a complete and polished application, but about showing us that you can design an application from the ground up. We have intentionally left the specification open to interpretation to give you room to be creative but also to determine some suitable limits of the application. There are no absolute right and wrong answers to this exercise.

Please keep in mind:

* Code quality matters
* Please document well; preferably in markdown
* Testability is important
