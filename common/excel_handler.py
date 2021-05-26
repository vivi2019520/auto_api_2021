#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:excel_handler.py
@time:2021/05/13
"""

import openpyxl
from config.path import Config


class ExcelHandler:

    def __init__(self, file):

        self.file = file

    def open_excel(self, sheet_name):
        """读取Excel，返回sheet对象"""
        workbook = openpyxl.load_workbook(self.file)
        sheet = workbook[sheet_name]
        return sheet

    def get_header(self, sheet_name):
        sheet = self.open_excel(sheet_name)
        header = []
        for i in sheet[1]:
            header.append(i.value)
        return header

    def read_excel(self, sheet_name):

        sheet = self.open_excel(sheet_name)
        rows = list(sheet.rows)
        data = []
        for row in rows[1:]:
            row_data = []
            for cell in row:
                row_data.append(cell.value)
                data_dict = dict(zip(self.get_header(sheet_name),row_data))
            data.append(data_dict)
        return data


if __name__ == '__main__':
    excel = ExcelHandler(Config.case_data_path)
    data = excel.read_excel("login")
    print(data)
