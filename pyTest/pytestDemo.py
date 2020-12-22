import pytest

class testdemo:
    def test_a(self):
        print("----------->test_a")
        assert 1
    def test_b(self):
        print("----------->test_b")
        assert 0
    def test_c(self):
        print("------------>test_3")
        assert 1
if __name__ =='__main__':
    #pytest.main(["-s", "pytestDemo.py"])
    #pytest.main(['-x','pytestDemo.py'])  #第01次失败，就停止测试
    #pytest.main(['--maxfail=2','pytestDemo.py'])#出现2个失败就终止测试
    #pytest.main(['pytestDemo.py'])#指定测试模块
    #pytest.main(['-k','Myclass and not method','pytestDemo.py'])
    #通过关键字表达式过滤执行 这条命令会匹配文件名、类名、方法名匹配表达式的用例，这里这条命令会运行 TestMyClass.test_something， 不会执行 TestMyClass.test_method_simple
    pytest.main(["-s","pytestDemo.py","--reruns","2","--reruns-delay","5"])