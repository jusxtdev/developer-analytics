from agent import Agent
from config import ConfigManager
from event import Event
from session import Session


def main():
    config_manager = ConfigManager()

    agent = Agent(config_manager.get_config())
    session = Session()
    event = Event()

    agent.initialize(event)

    agent.run(event, session)


main()
