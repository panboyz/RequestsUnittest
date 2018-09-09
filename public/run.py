#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 验证包：接口测试脚本

import sys
import public.log1 as log
import main.common as common

logging = log.getLogger()

"""1.外部输入参数"""
path = sys.path[0]  # 当前路径
module = sys.argv[1]  # 服务模块名
url = sys.argv[2]  # 服务地址
host = sys.argv[3]  # 数据库地址
user = sys.argv[4]  # 数据库用户名
password = sys.argv[5]  # 数据库密码
db = sys.argv[6]  # 数据库名称

"""2.根据module获取Sheet"""
logging.info("-------------- Execute TestCases ---------------")
sheet = common.getExcelSheet(path + "/" + common.filename, module)

"""3.数据准备"""
logging.info("-------------- Prepare data through MysqlDB --------------")
sql = common.getPrepareSql(sheet)
common.prepareData(host=host, user=user, password=password, db=db, sql=sql)

"""4.执行测试用例"""
res = common.runTest(sheet, url)
logging.info("-------------- Get the result ------------ %s", res)
