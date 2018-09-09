# -*- coding: UTF-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/23 08:30

"""
import xlrd

workbook = None


def open_excel(path):
    """打开excel"""
    global workbook
    if workbook is None:
        workbook = xlrd.open_workbook(path, on_demand=True)
    return workbook


def get_sheet(sheetid):
    """获取行号"""
    global workbook
    return workbook.sheet_by_index(sheetid)


def get_rows(sheet):
    """获取行号"""
    return sheet.nrows


def get_cols(sheet):
    """获取行号"""
    return sheet.ncols


def get_content(sheet, row, col):
    """获取表格中内容"""
    return sheet.cell(row, col).value


def release(path):
    """释放excel减少内存"""
    global workbook
    workbook.release_resources()
    del workbook
