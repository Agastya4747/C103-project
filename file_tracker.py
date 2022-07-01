import sys
import time
import random
import os
import shutil 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/agast/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"the,{event.src_path} has been created")
    def on_deleted(self,event):
        print(f"the,{event.src_path} has been deleted")
    def on_modified(self,event):
        print(f"the,{event.src_path} has been modified")
    def on_moved(self,event):
        print(f"the,{event.src_path} has been moved to {event.dest_path}")

EventHandler = FileEventHandler()
observer = Observer()
observer.schedule(EventHandler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()
