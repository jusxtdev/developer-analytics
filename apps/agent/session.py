import time


class Session:
    def __init__(self):
        self.last_snapshot_time = time.time()
        self.last_upload_time = time.time()
