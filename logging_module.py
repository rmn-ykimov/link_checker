import logging

logger = logging.getLogger()


def log_error(logger, error_message: str):
    """
    Log an error message to the logger.
    :param logger: Logger object
    :param error_message: Error message to be logged
    """
    logger.error(error_message)


def handle_exception(func, logger):
    """
    Handle an exception by logging the error message to the logger.
    :param func: Function that may raise an exception
    :param logger: Logger object
    """
    try:
        func()
    except Exception as e:
        log_error(logger, str(e))
