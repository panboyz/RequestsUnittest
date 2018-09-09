# -*- coding:utf-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/22 08:13

"""
import os
import codecs
import configparser

proDir = os.path.dirname(os.path.dirname(__file__))
configPath = os.path.join(proDir, 'config/', "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath, 'rb')
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8')

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_case_param(self, name):
        value = self.cf.get("CASE", name)
        return int(value)
