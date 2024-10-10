import os
import sys, logging

from args import *
from bot import GhostLogger
from bot import BotManager

if __name__ == "__main__":
    logger = GhostLogger
    if "-v" in sys.argv or "--verbose" in sys.argv:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.ERROR)
        logger.addHandler(logging.StreamHandler())
        logger.addHandler(logging.FileHandler('.log'))
        formatter = logging.Formatter(
            "\033[91m[ERROR!]\033[0m %(asctime)s \033[95m%(message)s\033[0m"
        )
        logger.handlers[0].setFormatter(formatter)

    try:
        manager = BotManager()
        
        manager.start_selenium("1023")
        href = manager.action_1()
        manager.close_selenium("1023")
        
        manager.start_selenium("1023")
        href = manager.action_2(href)
        manager.close_selenium("1023")
        
        manager.start_selenium("1023")
        href = manager.action_3(href)
        manager.close_selenium("1023")
        
    except ValueError as e:
        print(f"Caught an error: {e}")
        sys.exit(1)

            
