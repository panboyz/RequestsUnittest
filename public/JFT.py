# -*- coding:utf-8 -*-

import os
import logging
import time

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]- %(levelname)s - %(filename)s:%(lineno)s - %(message)s')

# Init the log and set level
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set the log file
tim = time.strftime('%Y%m%d%H%M', time.localtime())
localpath = os.path.dirname(os.path.dirname(__file__))
file = tim + '.log'
filepath = os.path.join(localpath, 'Logs/', file)

# Add a FileHandler
fh = logging.FileHandler(filename=filepath, mode='w', encoding='utf-8')
formatter = logging.Formatter('[%(asctime)s]- %(levelname)s - %(filename)s:%(lineno)s - %(message)s')
fh.setFormatter(formatter)
fh.setLevel(logging.ERROR)
logger.addHandler(fh)

# Add a StreamHandler
sh = logging.StreamHandler()
sh_formatter = logging.Formatter('[%(asctime)s]- %(levelname)s - %(filename)s:%(lineno)s - %(message)s')
sh.setFormatter(sh_formatter)
sh.setLevel(logging.INFO)
logger.addHandler(sh)

# log the message
logger.debug('this is a debug message')
logger.info('this is a info message')
logger.warning('this is a warning message')
logger.error('this is a error message')
logger.critical('this is a critical message')
