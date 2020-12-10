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
import zipfile

import jsonpath
from loguru import logger

from api.comm.BaseRequest import BaseRequest
from api.utils.OperateDB import OperateDB
from api.utils.ReadConfig import ReadConfig
import pytest
import allure

#读取配置文件
from api.utils.ReadData import ReadData
from api.utils.SaveResponse import SaveResponse
from api.utils.TreatingData import TreatingData


rc = ReadConfig()
base_url = rc.read_server_config('test')
#获取token
token_reg = rc.read_response_reg() #, res_reg
log_path = rc.read_file_path('log_path')
report_data = rc.read_file_path('report_data')
report_generate = rc.read_file_path('report_generate')
case_data_path = rc.read_file_path('case_response_data')
case_db_path = rc.read_file_path('case_db_data')
report_zip = rc.read_file_path('report_zip')
email_setting = rc.read_email_setting()
db_setting = rc.read_db_setting()
#读取execl数据对象
data_response_list = ReadData(case_data_path).get_response_data()
#data_db_list = ReadData(case_db_path).get_Db_data("access_log")

#数据处理对象
treat_data = TreatingData()
#实例化响应的对象
save_response_dict = SaveResponse()
#请求对象
br = BaseRequest()
#数据库结果对象
operate_db = OperateDB(db_setting)




logger.info(f'配置文件/excel数据/对象实例化，等前置条件处理完毕\n\n')
@allure.feature('需求管理平台')
class TestApiAuto(object):
    data_db_list = ''
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
#    @pytest.mark.parametrize('case_number,type,value,condition,expect',data_db_list)
#    def test_db(self,case_number,type,value,condition,expect):
#        pass

#    @allure.story("二级标签")
    @pytest.mark.parametrize('case_number,case_title,path,is_token,method,parametric_key,file_var,'
                             'file_path,parameters,dependent,data,res_reg,expect,check_db',data_response_list)
    def test_main(self,case_number,case_title,path,is_token,method,parametric_key,file_var,
                  file_path,parameters,dependent,data,res_reg,expect,check_db):
        #动态添加标题
        allure.dynamic.title(case_title)

        logger.debug(f'***********...执行用例编号： {case_number} ...***********')

        with allure.step("处理相关数据依赖，header"):

            data,header,parameters_path_url = treat_data.treating_data(is_token,parameters,dependent,data,save_response_dict)

            allure.attach(json.dumps(header,ensure_ascii=False,indent=4),"请求头",allure.attachment_type.TEXT)
            allure.attach(json.dumps(data,ensure_ascii=False,indent=4),"请求数据",allure.attachment_type.TEXT)


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
                    treat_data.token_header['Authorization'] = "Bearer " +jsonpath.jsonpath(res,token_reg)[0]

        with allure.step("根据配置文件的提取响应规划提取实际数据"):

            if isinstance(res,list):
               pass
            if isinstance(res,dict):
                really = jsonpath.jsonpath(res,res_reg)
            if isinstance(res,str):
                pass
            allure.attach(json.dumps(really,ensure_ascii=False),"提取用于断言的实际响应部分数据",allure.attachment_type.TEXT)

        with allure.step("处理读取出来的预期结果响应"):
            #处理预期结果数据中使用True/False/None导致无法转换bug
            if 'None' in expect:
                expect = expect.replace('None','null')
            if 'True' in expect:
                expect = expect.replace('True','true')
            if 'False' in expect:
                expect = expect.replace('False','false')
            if isinstance(expect,dict):
                expect = json.loads(expect)
            allure.attach(json.dumps(expect,ensure_ascii=False,indent=4),"测试结果",allure.attachment_type.TEXT)
            
        with allure.step("预期结果与实际响应进行断言操作"):
            logger.info(f'完整的json响应：{res}\n需要校验的数据字典:{really}预期校验的数据字典：{expect}\n测试结果：{really == expect}')
            logger.debug(f'********...用例编号：{case_number},执行完毕，日志查看...********\n\n')
            allure.attach(json.dumps(expect,ensure_ascii=False,indent=4),"测试结果",allure.attachment_type.TEXT)
            if isinstance(expect,list):
                assert really == expect
            #assert set(expect.items()).issubset(set(really.items()))

        with allure.step("预期数据与实际结果进行断言操作"):
            if check_db:
                table_list = check_db.split("|")

                for table in table_list:
                    global data_db_list
                    table_name = table.split(':')[0]
                    data_id = table.split(':')[1]

                    data_db_list = ReadData(case_db_path).get_Db_data(table_name,int(data_id))
                    if data_db_list:
                        logger.info(f'数据列表信息：{data_db_list}\n')
                        TestApiAuto().test_db(data_db_list)
                    else:
                        logger.error("未查到数据")

            else:
                logger.info(f'没有添加数据库数据校验')

    @pytest.mark.parametrize('data_db_list',data_db_list)
    def test_db(self,data_db_list):

        effect_row,effect_reslut = operate_db.query_db(data_db_list[0][2],data_db_list[0][3],data_db_list[0][4])
        logger.info(f'返回结果数量:{effect_row}\n完整的数据库结果：{effect_reslut}\n预期校验的数据字典：{data_db_list[0][5]}\n测试结果：{effect_row == data_db_list[0][5]}')
        allure.attach(json.dumps(data_db_list[0][5],ensure_ascii=False,indent=4),"测试结果",allure.attachment_type.TEXT)





if __name__ == '__main__':
    TestApiAuto().runTest()

    # 使用jenkins集成将不会使用到这两个方法（邮件发送/报告压缩zip）
    from api.utils.ZipFile import zipDir
    from api.utils.SendEmail import SendEmail

    report_generate = os.path.join('../',report_generate)
    zipDir(report_generate,report_zip)
    #zip = zipfile.ZipFile('../result/report/apiAutoTestReport.zip', 'w', zipfile.ZIP_DEFLATED)
#    SendEmail(email_setting)
#    OperateDB()