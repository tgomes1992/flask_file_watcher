from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler , FileCreatedEvent , FileModifiedEvent
import os
import shutil
from concurrent.futures import ThreadPoolExecutor 
import time
import threading
from collections import deque

class MonitorPastas(FileSystemEventHandler):
    
    
    def __init__(self , time):
        self.events = deque()
        self.time = time
        self.executor = ThreadPoolExecutor(max_workers=5)
        self.lock = threading.Lock()
        self.processing = False
        
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".txt"):
            print(f"File {event.src_path} has been modified!")
            
    def on_created(self, event: FileSystemEvent):

        self.add_events(event)   
        print (len(self.events))
    
    def add_events(self , event):
        with self.lock:
            self.events.append(event)
            if not self.processing:
                self.processing = True
                self.executor.submit(self.batch_process)

        
    
    def batch_process(self):
        while True:
            print ("batch iniciado")
            time.sleep(self.time)
            with self.lock:
                if not self.events:
                    self.processing = False
                    break
                batch = list(self.events)
                self.events.clear()
            self.process_events(batch)
            
    def process_events(self, events):
        print(f"Processing batch of {len(events)} events")
        for event in events:

            if isinstance(event, FileCreatedEvent):
                print (event.src_path)
                shutil.move(event.src_path , os.path.join("C://moved", event.src_path.split("\\")[-1]))  
        # Simulate some processing time
        print("Batch processing complete")
        
        
