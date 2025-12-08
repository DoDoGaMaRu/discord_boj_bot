import os
import logging

DEBUG = os.getenv("DEBUG") == "True"

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)