#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
@project:autoTest
@file:readConfig.py
@time:2020/11/25
'''
import yaml
from loguru import logger


class readConfig(object):
    data = None

    @logger.catch
    def __init__(self):
        #读取yaml文件配置信息，初始化配置
        with open('../config/config.yaml','r',encoding='utf-8') as file:
            self.data = yaml.load(file.read(),Loader=yaml.FullLoader)

    @logger.catch
    def readFilePath(self,filePathName):
        return self.data.get('filePath').get(filePathName)