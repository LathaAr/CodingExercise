### Wireless APs

#### Description:

I have assumed that two processes are present in the same computer and implemented using the concept of Local-IPC(shared memory).The monitor ( ) is one process which monitors the Wireless_APs JSON file. And logger ( ) is another process to display the changed data in the Wireless_APs JSON file after few seconds. 

The monitor ( ) continuously/periodically monitors the JSON file for any modification. Once JSON file is modified, the monitor ( ) process informs the logger ( ) process to display the changes that are in Wireless_APs JSON file

##### Installed and used below python modules:

- For processes communications using Multiprocessing - Process, Queue
- For Continuous monitoring of JSON using watchdog.observers - Observer
- for Event handling on specific file using watchdog.events - FileSystemEventHandler
- To copying files using shutil - copyfile
- For JSON file parsing using json
- To Compare Json files (dictionary files) using dictdiffer

##### Implemented below files

- Json file - WirelessAP.json
- Python script - WirelessAPs_Monitor_logger.py

##### Open Command Prompt (cmd), run below commands to install modules

```
python -m pip install json
python -m pip install pprint
python -m pip install dictdiffer
python -m pip install watchdog
python -m pip install multiprocessing
python -m pip install shutil
```

##### Execution Output display in Console:

```
Open C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json
```

```
{
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

##### Modify WirelessAP.json file after few seconds

```
Open C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json
```

```
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

##### During execution generated 2 Json files for before and after event trigger (file modification)

- C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json

- C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json

  #### Execution output :

```
Microsoft Windows [Version 10.0.17134.472]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\latha>C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_logger.py

DEBUG:  Currently no_modification in json file

DEBUG:  Copied json file before file modification

DEBUG:  event type: modified  path : C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:  event type: modified  path : C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:  Copied json file after file modification

DEBUG:  Wireless APs in JSON format before event triggered:
{'access_points': [{'channel': 11, 'snr': 63, 'ssid': 'MyAP'},
                   {'channel': 1, 'snr': 42, 'ssid': 'YourAP'},
                   {'channel': 6, 'snr': 54, 'ssid': 'HisAP'}]}

DEBUG:  Wireless APs in JSON format after event triggered(after few seconds):
{'access_points': [{'channel': 11, 'snr': 82, 'ssid': 'MyAP'},
                   {'channel': 6, 'snr': 42, 'ssid': 'YourAP'},
                   {'channel': 1, 'snr': 71, 'ssid': 'HerAP'}]}

DEBUG:  Display surrounding Wireless APs

MyAP'S snr changed from 63  to 82
YourAP'S channel changed from 1  to 6
HisAP is removed from the list
HerAP is added to the list with SNR 71 and Channel 1

Process finished with exit code 0
```





