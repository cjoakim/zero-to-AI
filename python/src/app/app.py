import logging
import os
import sys
import time
import traceback

import asyncio

from dotenv import load_dotenv
from src.os.system import System

# This class is used to read the host environment variables.
# It also has methods for command-line flag argument processing.
# Chris Joakim, 3Cloud/Cognizant, 2026


class App:
    @classmethod
    def initialize(cls) -> None:
        try:
            logging.error("App#initialize - load_dotenv starting")
            load_dotenv(override=True)
            logging.error("App#initialize - load_dotenv completed")
            cls.set_event_loop_policy()
            return True
        except Exception as e:
            logging.error(f"App#initialize - Error initializing application: {e}")
            return False

    @classmethod
    def set_event_loop_policy(cls) -> bool:
        """
        Set the event loop policy for the current platform so as to support
        asynchronous operations with the await/async pattern.
        """
        if str(sys.platform) == "win32":
            try:
                logging.warning("System#set_event_loop_policy - Running on Windows")
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                logging.warning(
                    "System#set_event_loop_policy - WindowsSelectorEventLoopPolicy has been set"
                )
                return True
            except Exception as e:
                logging.error(
                    f"System#set_event_loop_policy - Error setting WindowsSelectorEventLoopPolicy: {e}"
                )
                return False
        else:
            logging.warning("System#set_event_loop_policy - Not running on Windows")
            return False
