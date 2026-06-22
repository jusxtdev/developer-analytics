from agent import Agent
from services.buffer import Buffer
from services.config import ConfigManager
from services.event import Event
from services.instance_manager import InstanceManager
from services.session import Session
from utils.logger_config import setup_logging


def main():
    setup_logging()

    InstanceManager.check_instance()

    config_manager = ConfigManager()

    buffer = Buffer()
    session = Session()
    event = Event()

    agent = Agent(config_manager.get_config(), session, event, buffer)

    agent.initialize()

    agent.run()

    InstanceManager.release_instance()


main()
