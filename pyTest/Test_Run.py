#coding=GBK
'''
import pytest
import allure
#from test_api.run.run import Test_run
#from test_api.data.get_cookies_value import get_cookies_value
import warnings
import os

@allure.feature('test-api')  # feature定义功能
class Test_Run():
    def setup_method(self, method):  #每个模块开始之前都会执行
        print('start.....')

   # @allure.story('登录/获取报文')  # story定义用户场景
    def test_1(self, true=None):
        warnings.simplefilter("ignore", ResourceWarning)
        # get_cookies_value()
        #a=Test_run()
        #a.run()
        #断言
        assert true

   def teardown_method(self, method):  ##每个模块结束之后都会执行
        print('end.....')

if __name__ == '__main__':
    # 生成配置信息 "-s 代表可以将执行成功的案例日志打印出来 ; -q+文件执行路径 代表只需要执行的文件"
    pytest.main(['-s','-q',r'pyTest.py','--alluredir','./report/html'])
    #os模块运行allure命令，来生成html格式的报告（根据刚刚生成的配置信息）
    os.system("E:/python37/Lib/site-packages/allure-2.8.0/bin/allure.bat "
              "generate "
               "./report/html"
               "-o "
              "./report/html")

'''