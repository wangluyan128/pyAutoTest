import os

import pytest
import allure
@allure.feature("这是登录模块测试用例")
class Test_login():
    @allure.story("用户名正确，登录成功")
    @allure.severity(allure.severity_level.BLOCKER) #堵塞
    def test_logina(self):
        allure.attach("这是一个纯文本",name="文本信息",attachment_type=allure.attachment_type.TEXT)#添加文本
        print("这是登录，用户名正确，登录成功")
        pass

    @allure.story("密码正确，登录成功")
    @allure.severity(allure.severity_level.CRITICAL) #严重
    def test_loginb(self):
        allure.attach("<body>这是一个网页</body>",name="HTML测试模块",attachment_type=allure.attachment_type.HTML)
        print("这是登录，密码正确，登录成功")
        pass
    @allure.story("用户名错误，登录失败")
    # --allure-link-pattern = issure:https://blog.csdn.net/weixin_44275820/article/details/105169871/issue/{}
    @allure.issue("10086","这是一个bug,需要修复")
    @allure.severity(allure.severity_level.NORMAL)
    def test_loginc(self):
        allure.attach.file("./picture/微信头像.jpg",attachment_type=allure.attachment_type.JPG)    #添加图片
        print("这是登录，用户名错误，登录失败")
        pass

    @allure.story("密码错误，登录失败")
    @allure.link("https://blog.csdn.net/weixin_44275820/article/details/105169871",name="我的博客")
    @allure.severity(allure.severity_level.MINOR)    #不太重要
    def test_logind(self):
        with allure.step("点击用户名输入框"):
            print("输入用户名")
        with allure.step("点击输入密码输入框"):
            print("输入密码")
        print("点击登录按钮")
        with allure.step("点击登录后登录失败"):
            assert "1" == 1
            print("这是登录，密码错误，登录失败")
        pass

    Testcase_link = "https://blog.csdn.net/weixin_44275820/article/details/105169871"
    @allure.story("用户不存在，登录失败")
    @allure.testcase(Testcase_link,"我的博客管理平台")
    @allure.severity(allure.severity_level.TRIVIAL)    #不重要
    def test_logine(self):
        print("这是登录，用户不存在，请重新注册")
        pass

    @allure.story("密码已锁定，登录失败")
    def test_loginf(self):
        print("这是登录，密码已锁定，请重置密码")
        pass

    @allure.story("密码为空，登录失败")
    def test_loging(self):
        print("这是登录，密码为空，请输入密码")
        pass

if __name__ =='__main__':
    pytest.main(["-v","-s","--alluredir","./result/html"])
    #os.system(f'allure serve ./result')
    #os.popen('allure serve ./result').read()
    #print(os.popen('dir').read())
    #os.system(r"C:\Users\DM\AppData\Local\Programs\Python\Python36\Lib\site-packages\allure-2.13.7\bin/allure.bat "
     #         "generate "    #allure转换命令：allure generate allure源文件目录 -o 转换后目录
     #         "E:/pyAutoTest/pyTest/result/"
     #         "-o "
     #         "E:/pyAutoTest/pyTest/result/html")
    os.system('allure generate ./report/html -o ./report/html/ --clean')
'''
实例2：

import pytest
import allure
import time
from selenium import webdriver

Testcase_link1 = "https://www.baidu.com"
@allure.testcase(Testcase_link1,"百度，你值得拥有")
@allure.feature("百度搜索")
@pytest.mark.parametrize("search_data",["奔驰","宝马","保时捷"])
def test_search(search_data):

    with allure.step("打开百度网页"):
        driver = webdriver.chrome("C:\\Users\liwenliang\AppData\Local\Google\Chrome\Application\chrome.exe")
        driver.get("https://www.baidu.com")

    with allure.step(f"输入搜索词",{Testcase_link1}):
        driver.find_element_by_id("KW").send_keys(search_data)
        time.sleep(3)
        driver.find_element_by_id("SU").click()
        time.sleep(3)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",name="这是保存的图片",attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()

if __name__ =='__main__':
    pytest.main("-v -s")
)
'''
