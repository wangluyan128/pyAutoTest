#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author:
@file: OperateDB.py
@time:
"""
import pymysql
from loguru import logger
from pymysql import OperationalError

from api.utils.ReadConfig import ReadConfig

#rc = ReadConfig()
#db_setting = rc.read_db_setting()
class OperateDB(object):

    def __init__(self,setting):
        logger.info(f'载入数据库初始化配置信息：{setting}')
        #连接数据库
        try:
            self.conn = pymysql.connect(host=setting['host'],port = setting['port'],user=setting['user'],passwd=setting['passwd'],db=setting['db'])
            self.cursor = self.conn.cursor()
        except OperationalError as e:
            print("Mysql Error %d: %s" %(e.args[0],e.args[1]))

    def query_db(self,table_name,value="*",query_condition=''):
        logger.info(f'查询条件：{table_name}|{value}|{query_condition}')
        #查询表数据
        if (value in [None,'']):
            value = "*"
        if  query_condition:
            result_sql ="select " + value + " from " + table_name +" where "+ query_condition
        else:
            result_sql = "select "+ value + " from " + table_name

        try:
            effect_row=self.cursor.execute(result_sql)
            effect_reslut = self.cursor.fetchall()
            logger.info(f'查询数据库返回结果为：{effect_reslut}')
            return effect_row,effect_reslut
        except Exception  as e:
            logger.error("Error %s for execute sql: %s" % (e, result_sql))
        finally:
            OperateDB.close

    def close(self):
        #关闭数据库连接
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
'''
    def clear_db(self,table_name):
        #初始化数据
        #清除表数据
        real_sql = "truncate table " +table_name +";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    def insert(self,table_name,table_data):
        #插入表数据
        real_sql = "INSERT INTO " + table_name + " VALUES(%r,%r,%r,%r,%r,%r,%r)" %(table_data)
        print(real_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()
        
    
'''





if __name__ == '__main__':
    print("hello world")
   # effect_row,effect_reslut=OperateDB(db_setting).query_db("access_log","","id =1")
   # print(effect_row)

