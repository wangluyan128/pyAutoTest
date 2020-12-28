#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author: yan
@file: BaseRequest.py
@time:
"""
import os

import filetype as filetype
import requests
from loguru import logger




class BaseRequest(object):
    def __init__(self):
        #整个接口测试中使用同一个session来管理cookies
        self.session = requests.Session()

    #请求
    def base_requests(self,method,url,parametric_key = None,data = None,file_var = None,file_path=None,header = None):
        '''

        :param method: 请求方法
        :param url: 请求url
        :param parametric_key:入参关键字，get/delete/head/options/请求使用params，
                post/put/patch请求可使用json（application/json)/data
        :param data: 参数数据，默认为None
        :param file_var: 接口中接受文件的参数关键字
        :param file_path: 文件对象的地址，单个文件直接放地址：/Users/XXX/Desktop/vue.js
                多个文件格式：["/Users/XXX/Desktop/vue.js","/Users/XXX/Desktop/jenkins.war"]
        :param header: 请求头
        :return: 返回json格式的响应
        '''
        session = self.session
        if(file_var in [None,'']) and (file_path in [None,'']):
            files = None
            #try:
            #    del treat_data.token_header['Content-Type']
            #except KeyError as e:
            #    logger.error(f'头文件尚无content-type属性，进入下一个检查，本轮值不发生变化：{e}')
        else:
            #文件不为空的操作
            if file_path.startswith('[') and file_path.endswith(']'):
                file_path_list = eval(file_path)    #字符串转成列表
                files = []
                #多文件上传
                for file_path in file_path_list:
                    files.append((file_var,(open(file_path,'rb'))))
            else:
            #    treat_data.token_header['Content-Type'] = "multipart/form-data"
                #单文件上传
                #files = {file_var:open(file_path,'rb')}
               # header['Content-Type'] = "multipart/form-data"
               #根据文件路径，自动获取文件名称和文件mineo类型
                a = filetype.guess(file_path)
                if a is None:
                    print('cannot guess file_path!')
                #媒体类型
                typee = a.mime
                #文件真实路径
                realp = os.path.realpath(file_path)
                #获取文件名
                fname = os.path.split(file_path)[-1]

                files ={"file":(file_var,open(file_path,'rb'),typee)}#"multipart/form-data"

        if parametric_key == 'params':
            res = session.request(method = method,url = url,params=data,headers = header)
        elif parametric_key == 'data':
            res = session.request(method = method,url = url,data = data,files = files,headers = header)
        elif parametric_key == 'json':
            res = session.request(method = method,url = url,json = data,files = files,headers = header)
        elif parametric_key == '':
            res = session.request(method = method,url = url,params=data,files = files,headers = header)
        else:
            raise ValueError('可选关键字为：get/delete/head/options/请求使用params,post/put/patch请求可使用json(application/json)/data')
        logger.info(f'请求方法：{method},请求路径：{url},请求参数：{data},请求文件：{files},请求头:{header}')
        return res.json()