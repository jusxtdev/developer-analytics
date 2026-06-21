import os
import sys


class InstanceManager:
    @staticmethod
    def check_instance(lock_file_path = 'agent.lock'):
        try:
            if os.path.exists(lock_file_path):
                print("Process already running")
                sys.exit(1)
            else:
                with open(lock_file_path, 'w') as file:
                    print("lock file created")
                    file.write(str(os.getpid()))
        except OSError as e:
            print(f"Failed to create lock file {e}")
            sys.exit(1)
            
    def release_instance(lock_file_path = 'agent.lock'):
        try:
            if (os.path.exists(lock_file_path)):
                os.remove(lock_file_path)
                print("Lock file removed")
            else:
                print("No lock file found to remove")
                sys.exit(1)
        except OSError as e:
            print(f"Failed to clear instance {e}")
            sys.exit(1)