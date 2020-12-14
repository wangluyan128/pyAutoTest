#!/usr/bin/env python
# -*- coding:utf-8 -*-
import operator
import random
from filecmp import cmp


def hello(name):
    strHello = "Hello, " + name
    return strHello


print(hello("Python!"))

import sys
from loguru import logger

# logger.debug("That's it ,beautiful and simple logging!")

# logger.add("file_{time}.log")
# logger.add("file_1.log",rotation="100kb")

# @logger.catch
# def my_function(x,y,z):
#    a = 1/(x+y+z)
#    logger.info(a)
#    return a

# a = my_function(1,1,-2)
# logger.info(a)

import pytest


def foo():  # 定义函数foo()，

    m = 3  # 定义变量m=3;

    def bar():  # 在foo内定义函数bar()

        n = 4  # 定义局部变量n=4

        print(m + n)  # m相当于函数bar()的全局变量

    bar()  # foo()函数内调用函数bar()


class A:
    def x(self):
        global aa
        aa = 1
        A.y

    # @pytest.mark.parametrize('e',aa)
    def y(self):
        # for i in range(10):
        self.x()
        #   b=i+self.a
        print("aaaa" + str(aa))


class b:
    name = "hello"

    def w(self):
        if 'a':
            for i in range(1):
                global name
                name = 'world'
                print(name)
                b().z(name)
        # return i

    k = 1
    print(name+"aaaa")
    @pytest.mark.parametrize('e', name)
    def z(self,e):
        print("eee"+name)


class sample_func():
    def __init__(self):
        self.a = 78
        self.b = range(5)

    def __call__(self):
        print(self.a, self.b, self.x)

def str1():
    l1 = ((1, '需求统计-统计用户需求花费工时(执行)'),)#.__str__()
    str1 = "1,需求统计-统计用户需求花费工时(执行)".split(",")
    l2 = list(l1)
    print(str1)
    list1 = list(l1[0])
    print(list(l1[0]))
    for n in range(len(list1)):
        if isinstance(list1[n],int):
            list1[n] = str(list1[n])
        else:
            print(list1[n])
    print(list1)
    print(str1 == list1)
    assert  str1 == list1

    #print(operator.eq(l1[0],l2))



if __name__ == '__main__':
    aa = str1()

