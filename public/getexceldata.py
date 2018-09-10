# -*- coding:utf-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/19 10:59

"""

import os
from public.excel import *
from public.log import Logger
from public.getconfig import ReadConfig

cf = ReadConfig()
log = Logger()


basedir = os.path.dirname(os.path.dirname(__file__))
excelfile = os.path.join(basedir, 'testdata/', 'case.xlsx')
workbook = open_excel(excelfile)
sheet_default = get_sheet(0)


def read_excel_data(sheet_num, row_num, col_num):
    basedir = os.path.dirname(os.path.dirname(__file__))
    xlsxfiledir = os.path.join(basedir, 'testdata/', 'case.xlsx')
    if not os.path.exists(xlsxfiledir):
        log.info('%s 目录或文件不存在，准备新建' % xlsxfiledir)
        try:
            fobj = open(xlsxfiledir, 'w')
            fobj.close()
            log.info('case.xlsx新建成功')
        except Exception as e:
            log.error('异常, %s' % e)
    else:
        sheet = workbook.get_sheet(sheet_num)
        datarow = sheet.row(row_num)[col_num].value
        return datarow


def get_excel_data(param):

    nrows = get_rows(sheet_default)
    row_0 = sheet_default.row_values(0)

    if param != 'all':
        if isinstance(type(param), int) and 1 <= param <= (nrows - 1):
            caseurl = get_content(sheet_default, param, cf.get_case_param('case_url'))
            casemethod = get_content(sheet_default, param, cf.get_case_param('case_method'))
            caseheader = get_content(sheet_default, param, cf.get_case_param('case_header'))
            casedata = get_content(sheet_default, param, cf.get_case_param('case_data'))
            caseassert = get_content(sheet_default, param, cf.get_case_param('case_assert'))
            caseexcept = get_content(sheet_default, param, cf.get_case_param('case_except'))

            return caseurl,casemethod,caseheader,casedata,caseassert,caseexcept
        else:
            log.error('参数%s有误' % param)
    else:
        sum_data_list = list()
        single_data_dict = dict()
        for i in range(1, nrows):
            for j in range(2, len(row_0)):
                single_data_dict[row_0[j]] = get_content(sheet_default, i, j)
            sum_data_list.append(single_data_dict)
            single_data_dict = dict()
        return sum_data_list
