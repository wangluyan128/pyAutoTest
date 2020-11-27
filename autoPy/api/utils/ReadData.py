#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author: yan
@file: ReadData.py
@time: 2020/7/31
"""
import xlrd
from loguru import logger


class ReadData(object):
    def __init__(self,excelPath):
        self.excelFile = excelPath
        self.book = xlrd.open_workbook(self.excelFile)

    def get_data(self):
        '''

        :return:dataList - pytest参数化可用的数据
        '''
        data_list = []
        table = self.book.sheet_by_index(0)
        for nrow in range(1,table.nrows):
            #每行第4列 是否运行
            if table.cell_value(nrow,3) != '否': #每行第三列等于否将不读取内容
                value = table.row_values(nrow)
                value.pop(3)
                #配合将每一行转换成元组存储，适应pytest的参数化操作，如不需要可以注释掉value = tuple(value)
                value = tuple(value)
                logger.info(f'{value}')
                data_list.append(value)
        return data_list