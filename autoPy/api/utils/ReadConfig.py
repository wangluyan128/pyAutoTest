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
    def read_server_config(self,server_name):
        logger.info(self.data.get('server').get(server_name))
        return self.data.get('server').get(server_name)

    @logger.catch
    def read_file_path(self,file_path_name):
        return self.data.get('file_path').get(file_path_name)
    @logger.catch
    def read_server_reg(self):
        get_token = self.data.get("response_reg").get("token")
        get_resp = self.data.get("response_reg").get("response")
        logger.info(f'从响应中提取的token表达式：{get_token}')
        logger.info(f'从响应提取的需要校验的表达式：{get_resp}')
        return get_token,get_resp