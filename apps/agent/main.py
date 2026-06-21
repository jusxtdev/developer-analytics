import time
import psutil

from session import Session
from event import Event
from agent import Agent
from config import ConfigManager

def main():
    config_manager = ConfigManager()    
    
    agent = Agent(config_manager.get_config())
    session = Session()
    event = Event()
    
    agent.initialize(event)
    
    agent.run(event, session)

main()
