#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


class Test(object):

    @pytest.mark.run(order=3)
    def test_three(self):
        print("执行用例test_three")
        assert True

    @pytest.mark.run(order=4)
    def test_four(self):
        print("执行用例test_four")
        assert True

    @pytest.mark.run(order=2)
    def test_two(self):
        print("执行用例test_two")
        assert True

    @pytest.mark.run(order=1)
    def test_one(self):
        print("执行用例test_one")
        assert True


if __name__ == '__main__':
    pytest.main(['-s','Test1.py'])
    #pytest.main(['-s', 'Test1.py::Test::test_one'])
    #pytest.main(['-k','run or error and not list','--collect-only'])
    #pytest.main(['--html','report.html'])
    #t = Test()
