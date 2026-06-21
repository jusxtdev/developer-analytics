import time
from datetime import UTC
from datetime import datetime

import psutil
from win32 import win32gui
from win32 import win32process

from buffer import Buffer
from event import Event
from session import Session


class Agent:
    def __init__(self, config, session: Session, event: Event, buffer: Buffer):
        self.config = config
        self.session = session
        self.event = event
        self.buffer = buffer

    def get_poll_interval(self):
        return self.config["POLL_INTERVAL"]

    def get_snapshot_interval(self):
        return self.config["SNAPSHOT_INTERVAL"]

    def get_upload_interval(self):
        return self.config["UPLOAD_INTERVAL"]

    def initialize(self):        
        self.pollOS()
        self.event.updateState()
        self.event.logEvent(self.buffer)

    def pollOS(self):
        
        # get the title of focused window
        hwnd = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(hwnd)

        # get application name of focused window
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)

        self.event.title = title
        self.event.application = process.name()
        self.event.timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        return

    def snapShot(self, now):
        # log the event on every 10 seconds (snapshot)
        if now - self.session.last_snapshot_time >= self.get_snapshot_interval():
            self.session.last_snapshot_time = now
            self.event.logEvent(self.buffer)

    def windowChange(self):
        # log the event on window change
        if self.event.last_title is not None:
            if (
                self.event.title != self.event.last_title
                and self.event.application != self.event.last_application
            ):
                self.event.updateState()
                self.event.logEvent(self.buffer)

    def upload(self, now):
        # Upload every 30 seconds
        if now - self.session.last_upload_time >= self.get_upload_interval():
            self.session.last_upload_time = now
            self.buffer.clear_buffer()
            print("Upload")

    def run(self):
        while True:
            self.pollOS()

            # get current time
            now = time.time()

            self.snapShot(now)

            self.windowChange()

            self.upload(now)

            time.sleep(self.get_poll_interval())
