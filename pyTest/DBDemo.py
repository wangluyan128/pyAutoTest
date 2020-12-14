#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
class DBConfig:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port = 3306,user='root',passwd="123456",db='dms')

        self.cursor = self.conn.cursor()

    def DB1(self):
        #创建链接

        #创建游标


        #执行SQL，并返回受影响行数
        effect_row = self.cursor.execute("select id,type,method from access_log")
        print(effect_row)
        print(self.cursor.fetchall())
        #执行SQL，并返回受影响行数
        #effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))
        #执行SQL，并返回受影响行数
        #effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
        #获取第一行数据
        row_1 = self.cursor.fetchone()
        #获取前n行数据
        row_2 = self.cursor.fetchmany(3)
        #获取所有数据
        row_3 = self.cursor.fetchall()
        #提交SQL，并返回受影响行数

        #在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：

        #cursor.scroll(1,mode='relative')  # 相对当前位置移动
        #cursor.scroll(2,mode='absolute') # 相对绝对位置移动
        self.conn.commit()

        #关闭游标
        self.cursor.close()
        #关闭链接
        self.conn.close()
    def db2(self):
        #获取新创建数据自增ID
        #创建链接
        conn = pymysql.connect(host='127.0.0.1',port = 3306,user='root',passwd='123456',db='dms')
        #创建游标
        cursor = conn.cursor()
        cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
        conn.commit()
        cursor.close()
        conn.close()
        #获取最新自增ID
        new_id = cursor.lastrowid
    def db3(self):
        #关于默认获取的数据是元祖类型，如果想要或者字典类型的数据
        #创建链接
        conn = pymysql.connect(host='127.0.0.1',port = 3306,user='root',passwd='123456',db='dms')
        #游标设置为字典类型
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        r = cursor.execute("call p1()")
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()



if __name__ == '__main__':
    DBConfig().DB1()