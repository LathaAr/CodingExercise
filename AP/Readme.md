### Wireless APs Websockets

#### Description:

I have implemented Wireless APs monitoring application and displays information in html page (browser). Implemented using websockets and asynchronous programming.

##### Installed and used below python modules:

- For browser and server communication implemented using websockets 
- For Asynchronous programming using asyncio
- For Continuous monitoring of JSON using watchdog.observers - Observer
- for Event handling on specific file using watchdog.events - FileSystemEventHandler
- To copying files using shutil - copyfile
- For JSON file parsing using json
- To Compare Json files (dictionary files) using dictdiffer

##### Implemented below files

- Json file - WirelessAP.json
- Python script - WirelessAPs_Monitor_Websockets.py
- Html file - Wireless_APs_Monitor.html

##### Open Command Prompt (cmd), run below commands to install modules

```
python -m pip install json
python -m pip install shutil
python -m pip install dictdiffer
python -m pip install watchdog
python -m pip install websockets
python -m pip install asyncio
```

##### Html file - Wireless_APs_Monitor.html

```
C:\Python37\MyScriptsSE\CodingExercise\AP\Wireless_APs_Monitor.html
```

##### Json file - WirelessAP.json

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

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json

#### Execution:

- ##### Run WirelessAPs_Monitor_Websockets.py in a terminal

```
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_Websockets.py
```

- ##### Open up the Wireless_APs_Monitor.html page in browser 

```
Latha joined the conversation

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification

DEBUG:	event_type	modified	in	src_path C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:	Copied json file after file modification

DEBUG:	Wireless APs in JSON format before event triggered: {"access_points": [{"ssid": "MyAP", "snr": 63, "channel": 11}, {"ssid": "YourAP", "snr": 42, "channel": 1}, {"ssid": "HisAP", "snr": 54, "channel": 6}]}

DEBUG:	Wireless APs in JSON format after event triggered(after few seconds): {"access_points": [{"ssid": "MyAP", "snr": 82, "channel": 11}, {"ssid": "YourAP", "snr": 42, "channel": 6}, {"ssid": "HerAP", "snr": 71, "channel": 1}]}

DEBUG:	Display surrounding Wireless APs

MyAP'S snr changed from 63 to 82

YourAP'S channel changed from 1 to 6

HisAP is removed from the list

HerAP is added to the list with SNR 71 and Channel 1

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification
```





