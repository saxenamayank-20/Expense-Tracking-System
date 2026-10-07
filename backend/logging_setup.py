import logging


def setup_logger(name, level=logging.DEBUG):
    # Log to stdout so messages show up in Render's log viewer.
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

    return logger
