from win32 import win32gui, win32process
from datetime import datetime, UTC
import time
import psutil

from session import Session
from event import Event

class Agent:
    def initialize(self, event:Event):
        self.pollOS(event)
        event.updateState()
        event.logEvent()
        
    
    def pollOS(self, event : Event):
        # get the title of focused window
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd)
        
        # get application name of focused window
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        
        event.title = title
        event.application = process.name()
        event.timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        return
    
    def snapShot(self, now, session : Session):
        # log the event on every 10 seconds (snapshot)
        if (now - session.last_snapshot_time >= 10):
            session.last_snapshot_time = now
            print("Snapshot")

    def windowChange(self, event : Event):    
        # log the event on window change
        if (event.last_title is not None):    
            if (event.title != event.last_title and event.application != event.last_application):
                event.updateState()
                print("Window Change")
            
    def upload(self, now, session :Session):
        # Upload every 30 seconds
        if (now - session.last_upload_time >= 30):
            session.last_upload_time = now
            print("Upload")
    
    def run(self, event:Event, session:Session):
        while (True):
            self.pollOS(event)

            # get current time
            now = time.time()
            
            self.snapShot(now=now, session=session)
            
            self.windowChange(event=event)
            
            self.upload(now=now, session=session)
                
            time.sleep(1)