"""
some module
"""

import logging
import os
from time import gmtime, strftime

log_filepath = './logs/'


def setup_logger(name, log_file, level=logging.INFO):
    """
    setup the logger

    Usage -
        ::code: python
            import logger

    :param str name: name of blah
    :param str log_file: flog file
    :param int level: logging level
    :return: logging object
    """
    '''
    level = logging.INFO
    try:
        os.makedirs(log_filepath)
    except Exception as e:
        pass

    handler = logging.FileHandler(log_filepath + log_file)
    formatter = logging.Formatter(
        '%(asctime)-8s | %(levelname)-6s | %(lineno)4s | %(filename)20s |%(funcName)15s() | %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
    '''
    logging.basicConfig(
    format='%(asctime)-8s | %(levelname)-6s | %(lineno)4s | %(filename)20s |%(funcName)15s() | %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
    )
    return logging



class LogFile:
    def __del__(self):
        del self.name

    def __init__(self, name):
        try:
            os.makedirs(log_filepath)
        except Exception as e:
            pass
        self.name = log_filepath + name + ".txt"

    def WriteLog(self, component, data):
        dt = strftime("%d-%m-%Y %H:%M:%S", gmtime())
        file = open(self.name, "a")
        dd = dt + "," + component + "," + str(data)
        file.write(dd)
        file.close()

    def WriteRaw(self, data):
        file = open(self.name, "a")
        file.write(data)
        file.close()


'''
self.LOG_CNT.basicConfig(#filename=log_filepath,
    filemode='a',
    #format='%(asctime)-8s | %(levelname)-6s | %(lineno)4s | %(filename)20s |%(funcName)15s() | %(message)s',
    format=' %(lineno)4s |%(funcName)15s() | %(message)s',
    datefmt='%H:%M:%S',
    level=self.LOG_CNT.DEBUG,
)
'''
'''CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0'''

'''
usage:
import Filelogger

logging_init = Filelogger.setup_logger('initFile_logger', 'InitLog.txt')
logging_init.info('__init__ file run')
'''
