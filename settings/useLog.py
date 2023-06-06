import logging as logging
from logging.handlers import TimedRotatingFileHandler
import os
import time
from utils.fileHeper import FileHelper


def get_filename(filename):
    # Get logs directory
    log_directory = os.path.split(filename)[0]

    # Get file extension (also it's a suffix's value (i.e. ".20181231")) without dot
    date = os.path.splitext(filename)[1][1:]

    # Create new file name
    filename = os.path.join(log_directory, date)

    # I don't want to add index if only one log file will exists for date
    if not os.path.exists('{}.log'.format(filename)):
        return '{}.log'.format(filename)

    # Create new file name with index
    index = 0
    f = '{}.{}.log'.format(filename, index)
    while os.path.exists(f):
        index += 1
        f = '{}.{}.log'.format(filename, index)
    return f


def init_log():
    """
    How to use
    try:
        1/0
    except ZeroDivisionError:
        logging.exception("message")
    logging.warning()    
    logging.info()    
   
    
    """

    format = u'%(asctime)s\t%(levelname)s\t%(filename)s:%(lineno)d\t%(message)s'
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    FileHelper.not_exist_create_folder("logs")

    # new file every minute
    rotation_logging_handler = TimedRotatingFileHandler('logs/log_init.json', 
                                when='D', 
                                interval=1, 
                                backupCount=5)
    rotation_logging_handler.setLevel(logging.DEBUG)
    rotation_logging_handler.setFormatter(logging.Formatter(format))
    rotation_logging_handler.suffix = '%Y%m%d'
    rotation_logging_handler.namer = get_filename

    logger.addHandler(rotation_logging_handler)

    return logger