from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler , FileCreatedEvent , FileModifiedEvent
from concurrent.futures import ThreadPoolExecutor 
from collections import deque
from .MonitorPastas import MonitorPastas

    
                
class MonitorPastasControl():
    
    
    def __init__(self) -> None:
        self.observer = Observer()
        self.eventMonitor = MonitorPastas(2)

    
    def start_monitor(self):

        self.observer.schedule(self.eventMonitor, "c://watcher", recursive=True)
        self.observer.start()


    def stop_monitor(self):
        
        self.observer.stop()
        
        