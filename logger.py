import logging
import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

LOGGING_FORMAT = os.getenv("LOGGING_FORMAT")
DEBUG_VALUE = os.getenv("DEBUG", "False") == "True"
if DEBUG_VALUE:
    LOGGING_LEVEL = "DEBUG"
else:
    LOGGING_LEVEL = "INFO"


def get_logger(name: str) -> logging.Logger:
    """Создаем логгер"""
    logger = logging.getLogger(name)
    logger.setLevel(LOGGING_LEVEL)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOGGING_LEVEL)
    formatter = logging.Formatter(LOGGING_FORMAT)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
