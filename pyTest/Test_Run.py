import os
import shutil

import pytest
import allure
@allure.feature('这里是一级标签')
class Test_all():
    '''
allure用例描述：
使用方法                     参数值                参数说明

@allure.epic()                 epic描述            敏捷里面的概念，定义史诗，往下是feature
@allure.feature()              模块名称            功能点的描述，往下是story
@allure.story()                用户故事            用户故事，往下是title
@allure.title(用例的标题)       用例的标题            重命名html报告名称
@allure.testcase()            测试用例的链接地址    对应功能测试用例系统里面的case
@allure.issue()                缺陷                对应缺陷管理系统里面的链接
@allure.description()          用例描述            测试用例的描述
@allure.step()                 操作步骤            测试用例的步骤
@allure.severity()             用例等级            blocker，critical，normal，minor，trivial
@allure.link()                 链接                定义一个链接，在测试报告展现
@allure.attachment()           附件                报告添加附件
pytest默认按字母顺序去执行的（小写英文--->大写英文--->0-9数字）
用例之间的顺序是文件之间按照ASCLL码排序，文件内的用例按照从上往下执行。
setup_module->setup_claas->setup_function->testcase->teardown_function->teardown_claas->teardown_module
    '''
    @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")

    def test_setup(self):
        print("我就是打酱油的setup")
    @pytest.mark.run(order=1)
    @allure.step(title="run就是一个正常的方法.")
    def test_run(self):
        allure.attach("自定义描述1", "描述内容，自定义")
        print("我要运行")
        assert True

    @pytest.mark.run(order=2)
    def test_skip(self):
        print("我要跳过")

    @allure.severity(allure.severity_level.BLOCKER)  #严重级别
    @allure.testcase("http://www.baidu.com/", "测试用例的地址")
    @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
    @pytest.mark.run(order=3)
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
        print("111111111")
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