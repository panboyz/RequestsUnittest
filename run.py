# -*- coding:utf-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/19 16:39

"""

import os
import time
import datetime
import unittest
import HTMLTestRunner
from public.sendemail import *


def interface():
    new_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
    basedir = os.path.dirname(__file__)
    file_dir = os.path.join(basedir, 'testreport/')
    file_name = file_dir + new_time + 'report.html'
    base_name = os.path.basename(file_name)
    fp = open(file_name, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'接口自动化测试报告',
                                           description=u'demo项目自动化测试情况:')
    start_time = datetime.datetime.now()
    print('------ 准备执行，开始时间：%s ------\n' % start_time)
    file = os.path.join(basedir, 'testcase')
    suite = unittest.defaultTestLoader.discover(file, pattern='*.py')
    runner.run(suite)
    fp.close()
    end_time = datetime.datetime.now()
    print('\n------ 执行完成，结束时间：%s ------' % end_time)
    duration = end_time - start_time
    print('持续时间：%s\n' % duration)
    if file_name and base_name:
        send_email(file_name, base_name)


if __name__ == '__main__':
    interface()
