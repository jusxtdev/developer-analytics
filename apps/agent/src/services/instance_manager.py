import logging
import os
import sys

logger = logging.getLogger(__name__)


class InstanceManager:
    @staticmethod
    def check_instance(lock_file_path="src/data/agent.lock"):
        try:
            if os.path.exists(lock_file_path):
                print("Process already running")
                logger.info(f"Instance already running. Lock file found: {lock_file_path}")
                sys.exit(1)
            else:
                with open(lock_file_path, "w") as file:
                    logging.info(f"Lock file created: {lock_file_path}")
                    file.write(str(os.getpid()))
        except OSError as e:
            print("Failed to create lock file")
            logger.info(f"Failed to create lock file {e}")
            sys.exit(1)

    def release_instance(lock_file_path="src/data/agent.lock"):
        try:
            if os.path.exists(lock_file_path):
                os.remove(lock_file_path)
                print("Lock file removed")
                logger.info("Lock file removed")
            else:
                print("No lock file found to remove")
                logger.info("No lock file found to remove")
                sys.exit(1)
        except OSError as e:
            print("Failed to clear instance")
            logger.info(f"Failed to clear instance {e}")
            sys.exit(1)
