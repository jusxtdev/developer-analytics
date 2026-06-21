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

last_title = None

def main():
    # App loop that polls OS every 1 second
    while (True):
        title, application = pollOS()

        # get current timestamp
        timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # log the title on window change
        if (title != last_title):
            last_title = title
            event = {
                "timestamp" : timestamp,
                "windowTitle" : title,
                "application" : application
            }
            print(event)
            
        time.sleep(1)


def pollOS():
    # get the title of focused window
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    
    # get application name of focused window
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid)
    return title, process.name()
    

main()
