# This is python script to monitor the changes to a config file which contains surrounding Wireless APs in JSON format

import os
import time
import logging
import json
import config
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FORMAT = ('%(levelname) -10s %(asctime)s  %(name) -10s %(funcName) -15s %(lineno)  -5d: %(message)s')
logger = logging.getLogger(__name__)


class MyFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, method_to_call):
        self.__method_to_call = method_to_call

    def on_modified(self, event):
        files_to_react_on = ['config.py']
        if os.path.basename(event.src_path) in files_to_react_on:
            logger.debug('calling method')
            self.__method_to_call()
        else:
            logger.debug('just non interesting files changed')


class Parser(object):
    def __init__(self):
        logger.debug('parser init start')
        self.config = config.config_parser
        logger.debug('current config: %s' % (json.dumps(self.config)))
        filewatcher_event_handler = MyFileSystemEventHandler(self.load_config)
        filewatcher_observer = Observer()
        filewatcher_observer.schedule(filewatcher_event_handler, '.', recursive=False)
        filewatcher_observer.start()

    def load_config(self):
        logger.debug('load_config called')
        import config
        reload(config)
        self.config = config.config_parser
        logger.debug('new config: %s' % (json.dumps(self.config),))


def main():
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
    logger.debug('starting main')
    parser = Parser()
    while True:
        try:
            time.sleep(0.3)
        except(KeyboardInterrupt, SystemExit):
            exit()


if __name__ == '__main__':
    main()
