import logging
import time
from datetime import UTC
from datetime import datetime

import psutil
from win32 import win32gui
from win32 import win32process

from services.buffer import Buffer
from services.event import Event
from services.instance_manager import InstanceManager
from services.session import Session
from utils.idle import get_idle_duration

logger = logging.getLogger(__name__)


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

    def get_idle_interval(self):
        return self.config["IDLE_INTERVAL"]

    def initialize(self):
        logger.info("Agent Initialized")
        self.pollOS()
        self.event.updateState()
        self.event.logEvent(self.buffer)
        logger.info("Initial write Done")

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
                self.event.logEvent(self.buffer)
                logger.info(
                    "Window changed: '%s' -> '%s'",
                    self.event.last_title,
                    self.event.title,
                )
                self.event.updateState()

    def upload(self, now):
        # Upload every 30 seconds
        if now - self.session.last_upload_time >= self.get_upload_interval():
            self.session.last_upload_time = now
            self.buffer.clear_buffer()
            print("Upload")
            logger.info("Batch Uploaded")

    def detect_idle(self):
        idle_seconds = get_idle_duration()
        if idle_seconds <= self.get_idle_interval():
            self.event.isIdle = False
        else:
            self.event.isIdle = True

    def shutdown(self):
        # self.upload()
        logger.info("Shutting down")
        InstanceManager.release_instance()
        logging.info("Application shutdown successful")
        print("Application shutdown successful")
        time.sleep(1)

    def run(self):
        logger.info("Application Started")
        while True:
            self.pollOS()

            # get current time
            now = time.time()

            self.detect_idle()

            self.snapShot(now)

            self.windowChange()

            self.upload(now)

            time.sleep(self.get_poll_interval())
