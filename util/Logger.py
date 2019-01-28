import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("./results/udacity-automation.log", mode='w')
    # fileHandler = logging.FileHandler("udacity-automation.log", mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
