#coding=GBK
'''
import pytest
import allure
#from test_api.run.run import Test_run
#from test_api.data.get_cookies_value import get_cookies_value
import warnings
import os

@allure.feature('test-api')  # feature���幦��
class Test_Run():
    def setup_method(self, method):  #ÿ��ģ�鿪ʼ֮ǰ����ִ��
        print('start.....')

   # @allure.story('��¼/��ȡ����')  # story�����û�����
    def test_1(self, true=None):
        warnings.simplefilter("ignore", ResourceWarning)
        # get_cookies_value()
        #a=Test_run()
        #a.run()
        #����
        assert true

   def teardown_method(self, method):  ##ÿ��ģ�����֮�󶼻�ִ��
        print('end.....')

if __name__ == '__main__':
    # ����������Ϣ "-s ������Խ�ִ�гɹ��İ�����־��ӡ���� ; -q+�ļ�ִ��·�� ����ֻ��Ҫִ�е��ļ�"
    pytest.main(['-s','-q',r'pyTest.py','--alluredir','./report/html'])
    #osģ������allure���������html��ʽ�ı��棨���ݸո����ɵ�������Ϣ��
    os.system("E:/python37/Lib/site-packages/allure-2.8.0/bin/allure.bat "
              "generate "
               "./report/html"
               "-o "
              "./report/html")

'''