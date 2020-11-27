#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project:autoTest
@author:yan
@file:TestApi.py
@time:2020/11/25
"""
import os
import shutil
from loguru import logger
from api.utils.ReadConfig import ReadConfig
import pytest
import allure

#读取配置文件
from api.utils.ReadData import ReadData

rc = ReadConfig()
log_path = rc.read_file_path('log_path')
report_data = rc.read_file_path('report_data')
report_generate = rc.read_file_path('report_generate')
case_data_path = rc.read_file_path('case_data')
#读取execl数据对象
data_list = ReadData(case_data_path).get_data()
#数据处理对象
treat_data = TreatingData()
class TestApiAuto(object):
    #启动方法
    def runTest(self):
        if os.path.exists('../result/report') and os.path.exists('../result/logs'):
            shutil.rmtree(path='../result/report')
            shutil.rmtree(path='../result/logs')
        #日志存取路径
        logger.add(log_path,encoding='utf-8')
        #pytest比unittest更简化，方便
        #pytest.main(args = [f'--alluredir={report_data}'])
        pytest.main(["-s", "--alluredir", report_data])
        # 本地生成 allure 报告文件
        # os.system(f'allure generate {report_data} -o {report_generate} --clean')

        # 直接启动allure报告（会占用一个进程，建立一个本地服务并且自动打开浏览器访问，ps 程序不会自动结束，需要自己去关闭）
        os.system(f'allure serve {report_data}')
        logger.warning('报告已生成')

    @pytest.mark.parametrize('case_number,case_title,path,is_token,method,parametric_key,file_var,'
                             'file_path,parameters,dependent,data,expect',data_list)
    def test_main(self,case_number,case_title,path,is_token,method,parametric_key,file_var,
                  file_path,parameters,dependent,data,expect):
        #动态添加标题
        allure.dynamic.title(case_title)

        logger.debug(f'***********...执行用例编号： {case_number} ...***********')

        with allure.step("处理相关数据依赖，header"):
            data,header,parameters_path_url = treat_data
if __name__ == '__main__':
    TestApiAuto().runTest()