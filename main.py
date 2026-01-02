from dpe.configs.logger import get_logger

logger = get_logger("log_from_main")


if __name__ == "__main__":
    logger.debug("This is a debug message from main.py")
