import os
import shutil

import pytest
import allure
@allure.feature('这里是一级标签')
class Test_all():




    @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
    def test_setup(self):
        print("我就是打酱油的setup")

    @allure.step(title="run就是一个正常的方法.")
    def test_run(self):
        allure.attach("自定义描述1", "描述内容，自定义")
        print("我要运行")
        assert True

    #def test_skip(self):
    #    print("我要跳过")

    @allure.severity(allure.severity_level.BLOCKER)  #严重级别
    @allure.testcase("http://www.baidu.com/", "测试用例的地址")
    @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
    def test_error(self):
        with allure.attach("自定义描述1", "我需要让他进行错误"):
            print("我错误了")
            assert False


    @allure.title("用例标题0")
    @allure.description("这里是对test_0用例的一些详细说明")
    @allure.story("这里是第一个二级标签")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("这里是步骤说明一")
    @pytest.mark.parametrize('param1,param2',[(1,10),(2,20)])
    @pytest.mark.parametrize('param',['青铜','白银','黄金'])
    def test_0(self,param1,param2,param):
        print(param1)
        allure.attach('附件内容是：'+param,'我是附件名',allure.attachment_type.TEXT)
    @allure.title("用例标题1")
    @allure.story("这里是第一个二级标签")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("这里是步骤说明二")
    @pytest.mark.parametrize('param1',['value 1','value 2'])
    @pytest.mark.parametrize('param2',[True],ids=["这是一个有意思的操作"])
    @pytest.mark.parametrize('param3',[1])
    def test_1(self,param1,param2,param3):
        allure.attach.file(r'E:\Myproject/pytest-allure/test/test_1.jsp',
                           '我是附件截图的名字',attachment_type=allure.attachment_type.JPG)

    @allure.step('这里是操作步骤打印：name:"{0}",age:"{age}"')
    def step_with_title(self,name,age=0):
        pass

    @allure.title("用例标题2")
    @allure.story("这里是第二个二级标签")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.issue("http://baidu.com",name='点击我跳转百度')
    @allure.testcase('http://bug.com/user-login-Lw==.html',name='点击我跳转禅道')
    def test_2(self):
        self.step_with_title('张三')
        self.step_with_title('李四',20)
        self.step_with_title('王五',age=30)
    @allure.title("用例标题3")
    @allure.story("这里是第三个二级标签")
    def test_3(self):
        pass


    #执行命令 pytest test_1.py --allure-stories "这里是第二个二级标签", "这里是第三个二级标签"
    #@allure.story @allure.feature 还可以用来指定执行的case集合
    #使用@allure.severity装饰器
    #BLOCKER = 'blocker'　　中断缺陷（客服端程序无响应，无法执行下一步骤）
    #CRITICAL = 'critical'　　临界缺陷（功能点缺失）
    #NORMAL = 'normal'　　普通缺陷（数据计算错误）
    #MINOR = 'minor'　　次要缺陷（界面错误与ui需求不符）
    #TRIVIAL = 'trivial'　　轻微缺陷（必须项无提示，或者提示不规范）　
    #@allure.step（‘这里是操作步骤的描述： 获取参数一：“{0}”，获取参数二： “{1}” ’）
    #allure.attach(body, name, attachment_type, extension)

    #body - 要写入文件的原始内容。

    #name - 包含文件名的字符串

    #attachment_type- 其中一个allure.attachment_type值

    #extension - 提供的将用作创建文件的扩展名

    #或者 allure.attach.file(source, name, attachment_type, extension)
    #链接@allure.link  @allure.issue  @allure.testcase
if __name__ == '__main__':
    pytest.main(["-s","--alluredir","report/data/"])
    os.system(f'allure generate report/data/ -o report/html --clean')
    #os.system(f'allure serve report/')