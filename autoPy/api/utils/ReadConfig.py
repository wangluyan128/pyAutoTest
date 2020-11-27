#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
@project:autoTest
@file:ReadConfig.py
@time:2020/11/25
'''
import yaml
from loguru import logger


class ReadConfig(object):
    data = None

    @logger.catch
    def __init__(self):
        #读取yaml文件配置信息，初始化配置
        with open('../config/config.yaml','r',encoding='utf-8') as file:
            self.data = yaml.load(file.read(),Loader=yaml.FullLoader)

    @logger.catch
    def read_file_path(self,file_path_name):
        return self.data.get('file_path').get(file_path_name)