import logging
import time

logger = logging.getLogger(__name__)


class Session:
    def __init__(self):
        self.last_snapshot_time = time.time()
        self.last_upload_time = time.time()
        logger.info("New Session created")
