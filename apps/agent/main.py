import time
import psutil

from session import Session
from event import Event
from agent import Agent

def main():
    agent = Agent()
    session = Session()
    event = Event()
    
    agent.initialize(event)
    
    agent.run(event, session)

main()
