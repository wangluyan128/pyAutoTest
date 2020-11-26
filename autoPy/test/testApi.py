#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project:autoTest
@author:yan
@file:testApi.py
@time:2020/11/25
"""
import os
import shutil
from loguru import logger
from api.utils.readConfig import readConfig
import pytest
import allure

#读取配置文件
rc = readConfig()
logPath = rc.readFilePath('logPath')
reportData = rc.readFilePath('reportData')

class TestApiAuto(object):
    #启动方法
    def runTest(self):
        if os.path.exists('../result/report') and os.path.exists('../result/logs'):
            shutil.rmtree(path='../result/report')
            shutil.rmtree(path='../result/logs')
        #日志存取路径
        logger.add(logPath,encoding='utf-8')
        #pytest比unittest更简化，方便
        #pytest.main(args = [f'--alluredir={reportData}'])
        pytest.main(["-s", "--alluredir", reportData])
        # 本地生成 allure 报告文件
        # os.system(f'allure generate {report_data} -o {report_generate} --clean')

        # 直接启动allure报告（会占用一个进程，建立一个本地服务并且自动打开浏览器访问，ps 程序不会自动结束，需要自己去关闭）
        os.system(f'allure serve ../result/report/data/')
        logger.warning('报告已生成')
if __name__ == '__main__':
    TestApiAuto().runTest()