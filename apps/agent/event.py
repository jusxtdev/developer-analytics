class Event:
    def __init__(self):
        self.last_title = None
        self.title = None
        self.application = None
        self.last_application = None
        self.timestamp = None
    
    def logEvent(self):
        print("logged")
        
    def updateState(self):
        self.last_title = self.title
        self.last_application = self.last_application
        