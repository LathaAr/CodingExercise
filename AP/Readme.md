### Wireless APs Websockets

#### Description:

I have implemented Wireless APs monitoring application and displays information in html page (browser). Implemented using websockets and asynchronous programming.

Implementation takes care of ignoring the order mismatches.  Like if the same AP information is
present but only if order of the APs are changed then the module does not report any change.

Implemented basic front end html browser UI but implementation of websockets communication to server is pending.

##### Installed and used below python modules:

- For browser and server communication implemented using websockets 
- For Asynchronous programming using asyncio
- For Continuous monitoring of JSON using watchdog.observers - Observer
- for Event handling on specific file using watchdog.events - FileSystemEventHandler
- To copying files using shutil - copyfile
- For JSON file parsing using json
- To Compare Json files (dictionary files) using deepdiff - DeepDiff
- For text modification using re

##### Implemented below files

- Json file - WirelessAP.json
- Python script - WirelessAPs_Monitor_Websockets_UI.py
- Html file - Wireless_APs_Monitor.html
- Html file - monitor.html (basic front end page is developed)
- temp.txt - generates for read/write during execution & removed once the task is completed

##### Open Command Prompt (cmd), run below commands to install modules

```
python -m pip install json
python -m pip install shutil
python -m pip install deepdiff
python -m pip install watchdog
python -m pip install websockets
python -m pip install asyncio
python -m pip install re
```

#### Execution - Scenario1:

##### Modify json file with same content like change in the order of content

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

##### Modify WirelessAP.json file after few seconds with same content with order change

Here YourAP and HisAP locations are interchanged.  Even though the JSON file is modified the overall content is same.  

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
      "ssid": "HisAP",
      "snr": 54,
      "channel": 6
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 1
    }
  ]
}
```

##### During execution generated 2 Json files for before and after event trigger (file modification) 

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json

##### Run WirelessAPs_Monitor_Websockets.py in a terminal

```
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_Websockets_UI.py
```

##### Open up the Wireless_APs_Monitor.html page in browser 

```
Latha joined the conversation

Latha: Checking Wireless APs information

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification

DEBUG:	event_type	modified	in	src_path C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:	Copied json file after file modification

DEBUG:	Wireless APs json file contents are same even after file changes
```



#### Execution - Scenario2:

##### Modify json file with changing contents like changing (ssid/snr/channel) values in json file

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

#####  Modify WirelessAP.json file after few seconds with changing (ssid/snr/channel) values   

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

##### During execution generated 3 Json files for before and after event trigger (file modification), temp.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json

C:\Python37\MyScriptsSE\CodingExercise\AP\temp.json (file removed once the task is completed)

- ##### Run WirelessAPs_Monitor_Websockets.py in a terminal

```
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/AP/WirelessAPs_Monitor_Websockets_UI.py
```

- ##### Open up the Wireless_APs_Monitor.html page in browser 

```
Latha joined the conversation

Latha: Checking Wireless APs information

*************************************

Monitoring Wirelss APs in JSON file

*************************************

DEBUG:	Currently no_modification in json file

DEBUG:	Copied json file before file modification

DEBUG:	event_type	modified	in	src_path C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json

DEBUG:	Copied json file after file modification

DEBUG:	Wireless APs json file contnents are not same

DEBUG:	Wireless APs in JSON format before event triggered: { "0": { "ssid": "HisAP", "snr": 54, "channel": 6 }, "1": { "ssid": "MyAP", "snr": 63, "channel": 11 }, "2": { "ssid": "YourAP", "snr": 42, "channel": 1 } }

DEBUG:	Wireless APs in JSON format after event triggered(after few seconds): { "0": { "ssid": "HerAP", "snr": 71, "channel": 1 }, "1": { "ssid": "MyAP", "snr": 82, "channel": 11 }, "2": { "ssid": "YourAP", "snr": 42, "channel": 6 } }

DEBUG:	Display surrounding Wireless APs:

INFO:	"HisAP" is removed from the list

INFO:	"HerAP" is added to the list with SNR 71 and channel 1

INFO:	"MyAP"'s SNR has changed from 63 to 82

INFO:	"YourAP"'s channel has changed from 1 to 6
```





