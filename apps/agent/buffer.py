import json
import os


class Buffer:
    def __init__(self, file_path="buffer.json"):
        self.buffer_path = file_path
        self.create_buffer_file()

    def create_buffer_file(self):
        if not os.path.exists(self.buffer_path):
            with open(self.buffer_path, "a") as f:
                json.dump([], f)

    def append_to_buffer(self, event_obj):
        if not os.path.exists(self.buffer_path):
            self.create_buffer_file()
        data = []        
        try:
            with open(self.buffer_path, "r") as f:
                data = json.load(f)    
        except json.JSONDecodeError:
            with open(self.buffer_path, "a") as f:
                json.dump([], f)

        data.append(event_obj)
        with open(self.buffer_path, "w") as f:
            json.dump(data, f, indent=4)

    def clear_buffer(self):
        if os.path.exists(self.buffer_path):
            with open(self.buffer_path, "w") as f:
                json.dump([], f)
