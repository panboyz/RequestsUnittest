# -*- coding: UTF-8 -*-
"""

@author:  zhoubaoyu
@create:  2018/8/23 08:30

"""
import os
import time
import logging

file = time.strftime('%Y%m%d%H%M', time.localtime()) + '.log'
default_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs/', file)


class Logger(object):

    def __init__(self, filename=None, slevel=logging.INFO, flevel=logging.INFO):
        if filename is None:
            self.filename = default_file
        else:
            self.filename = filename
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] - %(filename)s:%(lineno)s - %(levelname)s - %(message)s')
        sh = logging.StreamHandler()
        fh = logging.FileHandler(self.filename, mode='w', encoding='utf-8')
        sh.setFormatter(fmt)
        fh.setFormatter(fmt)
        sh.setLevel(slevel)
        fh.setLevel(flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        return self.logger.debug(message)

    def info(self, message):
        return self.logger.info(message)

    def warn(self, message):
        return self.logger.warning(message)

    def error(self, message):
        return self.logger.error(message)

    def critical(self, message):
        return self.logger.critical(message)
