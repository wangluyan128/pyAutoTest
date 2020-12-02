#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project:autoTest
@author:yan
@file:TestApi.py
@time:2020/11/25
"""
import json
import os
import shutil
import sys

from jsonpath import jsonpath
from loguru import logger

from api.comm.BaseRequest import BaseRequest
from api.utils.ReadConfig import ReadConfig
import pytest
import allure

#读取配置文件
from api.utils.ReadData import ReadData
from api.utils.SaveResponse import SaveResponse
from api.utils.TreatingData import TreatingData

rc = ReadConfig()
base_url = rc.read_server_config('test')
token_reg, res_reg = rc.read_response_reg()
log_path = rc.read_file_path('log_path')
report_data = rc.read_file_path('report_data')
report_generate = rc.read_file_path('report_generate')
case_data_path = rc.read_file_path('case_data')
report_zip = rc.read_file_path('report_zip')
email_setting = rc.read_email_setting()
#读取execl数据对象
data_list = ReadData(case_data_path).get_data()
#数据处理对象
treat_data = TreatingData()
#实例化响应的对象
save_response_dict = SaveResponse()
#获取token
token_reg,res_reg = rc.read_server_reg()
#请求对象
br = BaseRequest()

logger.info(f'配置文件/excel数据/对象实例化，等前置条件处理完毕\n\n')

class TestApiAuto(object):
    #启动方法
    def runTest(self):
        if os.path.exists('../result/report') and os.path.exists('../result/logs'):
            shutil.rmtree(path='../result/report')
            shutil.rmtree(path='../result/logs')
            #print(os.path.basename(sys.argv[0]))

        #日志存取路径
        logger.add(log_path,encoding='utf-8')
        #pytest比unittest更简化，方便
        #pytest.main(args = [f'--alluredir={report_data}'])
        pytest.main(["-s",os.path.basename(sys.argv[0]),"--alluredir", report_data])
        # 本地生成 allure 报告文件
        os.system(f'allure generate {report_data} -o {report_generate} --clean')

        # 直接启动allure报告（会占用一个进程，建立一个本地服务并且自动打开浏览器访问，ps 程序不会自动结束，需要自己去关闭）
        #os.system(f'allure serve {report_data}')
        logger.warning('报告已生成')

    @pytest.mark.parametrize('case_number,case_title,path,is_token,method,parametric_key,file_var,'
                             'file_path,parameters,dependent,data,expect',data_list)
    def test_main(self,case_number,case_title,path,is_token,method,parametric_key,file_var,
                  file_path,parameters,dependent,data,expect):
        #动态添加标题
        allure.dynamic.title(case_title)

        logger.debug(f'***********...执行用例编号： {case_number} ...***********')


        with allure.step("处理相关数据依赖，header"):

            data,header,parameters_path_url = treat_data.treating_data(is_token,parameters,dependent,data,save_response_dict)
            allure.attach(json.dumps(header,ensure_ascii=False,indent=4),"请求头",allure.attachment_type.TEXT)
            allure.attach(json.dumps(data,ensure_ascii=False,indent=4),"请求数据",allure.attachment_type.TEXT)
'''
        with allure.step("发送请求，取得响应结果的json串"):
            allure.attach(json.dumps(base_url + path + parameters_path_url,ensure_ascii=False,indent=4),"最终请求地址",allure.attachment_type.TEXT)
            res = br.base_requests(method = method,url = base_url+path+parameters_path_url,parametric_key=parametric_key,file_var = file_var,file_path = file_path,
                                   data = data,header = header)
            allure.attach(json.dumps(res,ensure_ascii=False,indent=4),"实际响应",allure.attachment_type.TEXT)
        with allure.step("将响应结果的内容写入实际响应字典中"):
            save_response_dict.save_actual_response(case_key = case_number,case_response=res)
            allure.attach(json.dumps(save_response_dict.actual_response,ensure_ascii=False,indent=4),"实际响应字典",allure.attachment_type.TEXT)
            #写token的接口必须是要正确无误能返回token的
            if is_token =='写':
                with allure.step("从登录的响应中提取token到header中"):
                    treat_data.token_header['Authorization'] = jsonpath.jsonpath(res,token_reg)[0]
        with allure.step("根据配置文件的提取响应规划提取实际数据"):
            really = jsonpath.jsonpath(res,res_reg)[0]
            allure.attach(json.dumps(really,ensure_ascii=False,index = 4),"提取用于断言的实际响应部分数据",allure.attachment_type.TEXT)
        with allure.step("处理读取出来的预期结果响应"):
            #处理预期结果数据中使用True/False/None导致无法转换bug
            if 'None' in expect:
                expect = expect.replace('None','null')
            if 'True' in expect:
                expect = expect.replace('True','true')
            if 'False' in expect:
                expect = expect.replace('False','false')
            expect = json.loads(expect)
            allure.attach(json.dumps(expect,ensure_ascii=False,indent=4),"测试结果",allure.attachment_type.TEXT)
        with allure.step("预期结果与实际响应进行断言操作"):
            logger.info(f'完整的json响应：{res}\n需要校验的数据字典:{really}预期校验的数据字典：{expect}\n测试结果：{really == expect}')
            logger.debug(f'********...用例编号：{case_number},执行完毕，日志查看...********\n\n')
            allure.attach(json.dumps(really == expect,ensure_ascii=False,indent=4),"测试结果",allure.attachment_type.TEXT)
            assert really == expect

'''

if __name__ == '__main__':
    TestApiAuto().runTest()

    # 使用jenkins集成将不会使用到这两个方法（邮件发送/报告压缩zip）
    # from tools.zip_file import zipDir
    # from tools.send_email import send_email
    # zipDir(report_generate, report_zip)
    # send_email(email_setting)