#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project: apiAutoTest
@author:
@file: SendEmail.py
@ide:
@time:
"""
import yagmail
from loguru import logger

from api.utils.ReadConfig import ReadConfig

#rc = ReadConfig()
#email_setting = rc.read_email_setting()
def SendEmail(setting):
    '''
    入参一个字典
    :param user:发件人邮箱
    :param password:邮箱授权码
    :param host:发件人使用的邮箱服务 例如：smtp.163.com
    :param contents: 内容
    :param addresses: 收件人列表
    :param title: 邮件标题
    :param enclosures: 附件列表
    :return:
    '''
    yag = yagmail.SMTP(setting['user'],setting['password'],setting['host'])
    print(setting['addressees'])
    print(setting['title'])
    print(setting['contents'])
    #发送邮箱
    yag.send(setting['addressees'],setting['title'],setting['contents'],setting['enclosures'])
    #关闭服务
    yag.close()
    logger.info("邮件发送成功！")

if __name__ == '__main__':
    pass
    #SendEmail(email_setting)