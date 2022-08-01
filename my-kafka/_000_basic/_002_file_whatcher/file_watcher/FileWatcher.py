import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWatcher:
    def __init__(self, package_name):
        self.watch_dir = f'{os.getcwd()}/logs/{package_name}'
        print(self.watch_dir)
        self.observer = Observer()

    def run(self):
        handler = Handler()
        self.observer.schedule(handler, self.watch_dir, recursive=True)

        self.observer.start()
        try:
            while True:
                time.sleep(10)
        except Exception as e:
            self.observer.stop()
            print(e)
            self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self):
        self.bootstrap_server = "localhost:9092"

    def on_created(self, event):
        print(event)

    def on_modified(self, event):
        print(event)



if __name__ == '__main__':
    FileWatcher('hr-work').run()
