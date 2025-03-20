import logging

logging.basicConfig(
    filename="test.log",  # Log file name
    level=logging.INFO,  # Log level (INFO, ERROR, DEBUG, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)

class Logger:
    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)
