import time
from win32 import win32gui, win32process
import psutil
from datetime import datetime, UTC
import logging
'''
{
    "timestamp": "2026-06-20T10:00:00Z",
    "application": "chrome.exe",
    "windowTitle": "Twitter / X - Home",
    "isIdle": false
}
'''

'''
poll os every 1 second 
check snapshot time
'''

class Session:
    def __init__(self):
        self.last_snapshot_time = time.time()
        self.last_upload_time = time.time()
        
class Event:
    def __init__(self):
        self.last_title = None
        self.title = ""
        self.application = ""
        self.timestamp = None
        print("Session Started...")
    
    def logEvent(self):
        print("logged")


def main():
    session = Session()
    event = Event()
    
    # log first event
    pollOS(event)
    event.last_title = event.title
    event.logEvent()
    
    # App loop that polls OS every 1 second
    while (True):
        pollOS(event)

        # get current time
        now = time.time()
        
        snapShot(now=now, session=session)
        
        windowChange(event=event)
        
        upload(now=now, session=session)
            
        time.sleep(1)


def pollOS(event : Event):
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

def snapShot(now, session : Session):
    # log the event on every 10 seconds (snapshot)
    if (now - session.last_snapshot_time >= 10):
        session.last_snapshot_time = now
        print("Snapshot")

def windowChange(event : Event):
    # no log on
    
    # log the event on window change
    if (event.title != event.last_title and event.last_title is not None):
        event.last_title = event.title
        print("Window Change")

def upload(now, session :Session):
    # Upload every 30 seconds
    if (now - session.last_upload_time >= 30):
        session.last_upload_time = now
        print("Upload")

main()
