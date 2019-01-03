import json
import os
from pprint import pprint
import dictdiffer
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from multiprocessing import Process, Queue
from shutil import copyfile


class FileHandler(FileSystemEventHandler):
    event_type = ''

    def on_modified(self, event):
        print('DEBUG:\t'+f'event type: {event.event_type}  path : {event.src_path}' "\n")
        self.event_type = 'modified'
        return


def file_change_notification(acc_points_path, q):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=acc_points_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.2)
            if event_handler.event_type == 'modified':
                q.put('modified')
                event_handler.event_type = ''
                acc_points_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json'
                # A file which contains surrounding Wireless APs in JSON format after event triggered
                access_points_after_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json'
                # Copy json file after the event triggred
                copyfile(acc_points_file, access_points_after_event_file)
                print("DEBUG:\tCopied json file after file modification\n")
                break
    except KeyboardInterrupt:
        observer.stop()
    return


def json_compare(file1, file2):

    with open(file1) as f:
        data1 = json.load(f)
        print("DEBUG:\tWireless APs in JSON format before event triggered:")
        pprint(data1)
    with open(file2) as f:
        data2 = json.load(f)
        print("\nDEBUG:\tWireless APs in JSON format after event triggered(after few seconds):")
        pprint(data2)

    print("\nDEBUG:\tDisplay surrounding Wireless APs \n")
    new_ssid = ''
    for diff in list(dictdiffer.diff(dict(data1), dict(data2))):
        diff1 = diff[1:]  # access_points,(n), changed element, i -> i
        diff2 = diff1[0]  # access_point,n,changed_element
        diff3 = diff1[1]  # n->n

        if diff2[2] == 'ssid':
            print((data1['access_points'][diff2[1]]['ssid']) + ' is removed from the list')
            print((data2['access_points'][diff2[1]]['ssid']) + ' is added to the list with SNR ' + str(
                data2['access_points'][diff2[1]]['snr']) + ' and Channel ' + str(
                data2['access_points'][diff2[1]]['channel']))
            ssid_changed = diff2[1]
            new_ssid = (data2['access_points'][diff2[1]]['ssid'])
        else:
            if (new_ssid == (data2['access_points'][diff2[1]]['ssid'])) and (ssid_changed == diff2[1]):
                continue
            new_ssid = ''
            print((data2['access_points'][diff2[1]]['ssid']) + '\'' + 'S ' + diff2[2] + ' changed from ' + str(
                diff3[0]) + "  to " + str(diff3[1]))


def logger(q):
    if q.get() == 'modified':
        access_points_before_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json'
        access_points_after_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_after_event.json'
        json_compare(access_points_before_event_file, access_points_after_event_file)


def monitor(q):
    q.put('no_modification')
    msg = q.get()
    print('\nDEBUG:\tCurrently ' + msg + ' in json file\n')
    # A file which contains surrounding Wireless APs in JSON format
    acc_points_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\WAP\WirelessAP.json'
    acc_points_path, filename = os.path.split(acc_points_file)
    # A file which contains surrounding Wireless APs in JSON format before event triggered
    access_points_before_event_file = 'C:\Python37\MyScriptsSE\CodingExercise\AP\Access_points_before_event.json'
    # Copy json file before the event triggered
    copyfile(acc_points_file, access_points_before_event_file)
    print("DEBUG:\tCopied json file before file modification\n")
    file_change_notification(acc_points_path, q)


if __name__ == "__main__":

    q = Queue()

    # File change notification flag
    monitor_app = Process(target=monitor, args=(q,))
    logger_app = Process(target=logger, args=(q,))

    monitor_app.start()
    monitor_app.join()

    logger_app.start()
    logger_app.join()
