from agent import Agent
from buffer import Buffer
from config import ConfigManager
from event import Event
from instance_manager import InstanceManager
from session import Session


def main():
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
