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

    def get_response_data(self):
        '''

        :return:dataList - pytest参数化可用的数据
        '''
        data_list = []
        table = self.book.sheet_by_index(0)

        for nrow in range(1,table.nrows):
        #    if nrow in [1,4,5]:#range(1,6):
                #每行第4列 是否运行
                if table.cell_value(nrow,3) != '否': #每行第三列等于否将不读取内容
                    value = table.row_values(nrow)
                    value.pop(3)
                    #配合将每一行转换成元组存储，适应pytest的参数化操作，如不需要可以注释掉value = tuple(value)
                    value = tuple(value)
                    logger.info(f'{value}')
                    data_list.append(value)
        return data_list

    def get_Db_data(self,sheet_name,row_id):
        '''

        :return:dataList - pytest参数化可用的数据
        '''
        data_list = []
        table = self.book.sheet_by_name(sheet_name)
        #每行第6列 是否运行
        try:
            if table.cell_value(row_id,6) != '否': #每行第三列等于否将不读取内容
                value = table.row_values(row_id)
                value.pop(6)
                #配合将每一行转换成元组存储，适应pytest的参数化操作，如不需要可以注释掉value = tuple(value)
                value = tuple(value)
                logger.info(f'{sheet_name}{value}')
                data_list.append(value)
        except Exception as e:
            logger.error(f'数据表未发现数据，发现异常{e}')

        return data_list