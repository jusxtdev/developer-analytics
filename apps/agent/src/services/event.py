from services.buffer import Buffer


class Event:
    def __init__(self):
        self.last_title = None
        self.title = None
        self.application = None
        self.last_application = None
        self.timestamp = None
        self.isIdle = False

    def logEvent(self, buffer: Buffer):
        event_obj = {
            "timestamp": self.timestamp,
            "title": self.title,
            "application": self.application,
            "isIdle": self.isIdle,
        }
        buffer.append_to_buffer(event_obj)

    def updateState(self):
        self.last_title = self.title
        self.last_application = self.last_application
