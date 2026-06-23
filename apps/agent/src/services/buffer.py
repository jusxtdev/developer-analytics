import json
import logging
import os

logger = logging.getLogger(__name__)


class Buffer:
    def __init__(self, file_path="src/data/buffer.json"):
        self.buffer_path = file_path
        self.create_buffer_file()

    def create_buffer_file(self):
        if not os.path.exists(self.buffer_path):
            with open(self.buffer_path, "a") as f:
                json.dump([], f)
                logger.info(f"Buffer file created {self.buffer_path}")

    def append_to_buffer(self, event_obj):
        # create buffer file if not exists
        if not os.path.exists(self.buffer_path):
            self.create_buffer_file()

        # Load existing data from buffer to in-memory object
        # if file is not a valid json (tampered), overwrite the file to create empty array (valid json)
        data = []
        try:
            with open(self.buffer_path, "r") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            with open(self.buffer_path, "a") as f:
                json.dump([], f)

        # add new event to dat aobject and write
        data.append(event_obj)
        with open(self.buffer_path, "w") as f:
            json.dump(data, f, indent=4)
            logger.info("Buffered event for window '%s'", event_obj["title"])

    def clear_buffer(self):
        if os.path.exists(self.buffer_path):
            with open(self.buffer_path, "w") as f:
                json.dump([], f)
                logger.info("Cleared Buffer file")

    def get_buffer(self):
        data = []
        try:
            with open(self.buffer_path, "r") as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError:
            logger.info("Buffer not found")
            