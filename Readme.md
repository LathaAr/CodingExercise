### Description:

I have assumed that the monitor application code resides in the server where the JSON file is located.  And the display application
resides in client to print the changed data in the JSON file.
The monitor application continously/periodically monitors the JSON file for any modification.
Once JSON file is modified, the monitor application informs the display application to display the changes that are change in JSON file

Implemented two applications(present in same network) communication using python socket module
Implemented Continous monitor modification of JSON using python watchdog module


#### Note:
#### Issues that are face:
* In parser.py, after modification identifed, Load_config is not functioning. 
* Since config is not reloading, it is not displaying new config file (Json format) as output of parser.py

# Implemented below Python scripts 
* Monitor_App.py
* Display_App.py
* parse.py
* config.py


#### Open Command Prompt (cmd), run below commands to install
#### Modules to install for Monitor_App.py and Display_App.py
    python -m pip install Socket
    python -m pip install argparse
    
#### Modules to install for parser.py 
    python -m pip install watchdog

##Execution Output display in Console:
```markdown
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Python37\MyScriptsSE\CodingExercise\Development>C:\Python37\python.exe Monitor_App.py --port=9900
Starting up echo server on localhost port 9900
Waiting to receive message from client
Data: b'Test message. This will be echoed'
sent b'Test message. This will be echoed' bytes back to ('127.0.0.1', 55351)
Waiting to receive message from client
```
```markdown
C:\Python37\MyScriptsSE\CodingExercise\Development>C:\Python37\python.exe Display_App.py --port=9900
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Python37\MyScriptsSE\CodingExercise\Development>C:\Python37\python.exe Display_App.py --port=9900
Connecting to localhost port 9900
Sending Test message. This will be echoed
Received: b'Test message. This will be echoed'
Closing connection to the server
```
```markdown
C:\Python37\MyScriptsSE\CodingExercise\Development> 
open Config.py
Intial Config file Details:
```

```json
config_parser = {
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
```commandline
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/Development/parser.py
DEBUG      2018-12-01 19:36:08,452  __main__   main             48  : starting main
DEBUG      2018-12-01 19:36:08,452  __main__   __init__         30  : parser init start
DEBUG      2018-12-01 19:36:08,452  __main__   __init__         32  : current config: {"access_points": [{"ssid": "MyAP", "snr": 63, "channel": 11}, {"ssid": "YourAP", "snr": 42, "channel": 1}, {"ssid": "HisAP", "snr": 54, "channel": 6}]}
```


####Modified Config file to after few seconds: 
```json
config_parser = {
  "access_points": [
    {
      "ssid": "MyAP",
      "snr": 82,
      "channel": 11
    },
    {
      "ssid": "YourAP",
      "snr": 42,
      "channel": 1
    },
    {
      "ssid": "HerAP",
      "snr": 71,
      "channel": 1
    }
  ]
}
```
```commandline
Output:
C:\Python37\python.exe C:/Python37/MyScriptsSE/CodingExercise/Development/parser.py
DEBUG      2018-12-01 19:36:08,452  __main__   main             48  : starting main
DEBUG      2018-12-01 19:36:08,452  __main__   __init__         30  : parser init start
DEBUG      2018-12-01 19:36:08,452  __main__   __init__         32  : current config: {"access_points": [{"ssid": "MyAP", "snr": 63, "channel": 11}, {"ssid": "YourAP", "snr": 42, "channel": 1}, {"ssid": "HisAP", "snr": 54, "channel": 6}]}
DEBUG      2018-12-01 19:36:25,356  __main__   on_modified      25  : just non interesting files changed
DEBUG      2018-12-01 19:36:25,357  __main__   on_modified      25  : just non interesting files changed
DEBUG      2018-12-01 19:36:25,384  __main__   on_modified      25  : just non interesting files changed
DEBUG      2018-12-01 19:36:36,294  __main__   on_modified      25  : just non interesting files changed
DEBUG      2018-12-01 19:36:36,295  __main__   on_modified      25  : just non interesting files changed
DEBUG      2018-12-01 19:36:43,917  __main__   on_modified      25  : just non interesting files changed
DEBUG      2018-12-01 19:37:00,407  __main__   on_modified      25  : just non interesting files changed
```
