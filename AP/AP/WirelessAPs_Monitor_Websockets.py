import os
import json
import time
from shutil import copyfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import dictdiffer
import websockets
import asyncio


class FileHandler(FileSystemEventHandler):
    event_type = ''
    src_path = ''

    def on_modified(self, event):
        self.event_type = event.event_type
        self.src_path = event.src_path
        return


async def file_change_notification(websocket, acc_points_path, q):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=acc_points_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.2)
            if event_handler.event_type == 'modified':
                await websocket.send('DEBUG:\tevent_type\t' + event_handler.event_type+'\tin\t'+'src_path\t' + event_handler.src_path)
                await q.put('modified')
                event_handler.event_type = ''
                acc_points_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json'
                # A file which contains surrounding Wireless APs in JSON format after event triggered
                access_points_after_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json'
                # Copy json file after the event triggred
                copyfile(acc_points_file, access_points_after_event_file)
                await websocket.send("DEBUG:\tCopied json file after file modification\n")
                break
    except KeyboardInterrupt:
        observer.stop()
    return


async def json_compare(websocket, file1, file2):
    with open(file1) as f:
        data1 = json.load(f)
        data1_json = json.dumps(data1)
        await websocket.send('DEBUG:\tWireless APs in JSON format before event triggered:'+ "\n" + data1_json)
    with open(file2) as f:
        data2 = json.load(f)
        data2_json = json.dumps(data2)
        await websocket.send('\nDEBUG:\tWireless APs in JSON format after event triggered(after few seconds):'+"\n" + data2_json)
        await websocket.send("\nDEBUG:\tDisplay surrounding Wireless APs \n")
    new_ssid = ''
    for diff in list(dictdiffer.diff(dict(data1), dict(data2))):
        diff1 = diff[1:]  # access_points,(n), changed element, i -> i
        diff2 = diff1[0]  # access_point,n,changed_element
        diff3 = diff1[1]  # n->n

        if diff2[2] == 'ssid':
            await websocket.send((data1['access_points'][diff2[1]]['ssid']) + ' is removed from the list')
            await websocket.send((data2['access_points'][diff2[1]]['ssid']) + ' is added to the list with SNR ' + str(
                data2['access_points'][diff2[1]]['snr']) + ' and Channel ' + str(
                data2['access_points'][diff2[1]]['channel']))
            ssid_changed = diff2[1]
            new_ssid = (data2['access_points'][diff2[1]]['ssid'])
        else:
            if (new_ssid == (data2['access_points'][diff2[1]]['ssid'])) and (ssid_changed == diff2[1]):
                continue
            new_ssid = ''
            await websocket.send((data2['access_points'][diff2[1]]['ssid']) + '\'' + 'S ' + diff2[2] + ' changed from ' + str(
                diff3[0]) + "  to " + str(diff3[1]))


async def logger(websocket, q):
    if await q.get() == 'modified':
        access_points_before_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json'
        access_points_after_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json'
        await json_compare(websocket, access_points_before_event_file, access_points_after_event_file)


async def monitor(websocket, path):

    q = asyncio.Queue()
    await q.put('no_modification')
    msg = await q.get()

    name = await websocket.recv()
    global clients
    clients.add(websocket)
    for client in clients:
        await client.send("{} joined the conversation".format(name))
    while True:
        try:
            for client in clients:
                await client.send("*************************************")
                await client.send("Monitoring Wirelss APs in JSON file")
                await client.send("*************************************")
                await client.send('\nDEBUG:\tCurrently ' + msg + ' in json file\n')
                # A file which contains surrounding Wireless APs in JSON format
                acc_points_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json'
                acc_points_path, filename = os.path.split(acc_points_file)
                # A file which contains surrounding Wireless APs in JSON format before event triggered
                access_points_before_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json'
                # Copy json file before the event triggered
                copyfile(acc_points_file, access_points_before_event_file)
                await client.send("DEBUG:\tCopied json file before file modification\n")
                await file_change_notification(client, acc_points_path, q)
                await logger(client, q)
        except:
            clients.remove(websocket)


if __name__ == "__main__":
    clients = set()
    start_server = websockets.serve(monitor, 'localhost', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
