#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
@project:
@author:
@file: ZipFile_bak.py
@ide:
@time:
"""
import os
import zipfile


def zipDir(dirpath,outFullName):
    '''
    压缩指定文件夹
    :param dirpath:目标文件路径
    :param outFullName: 压缩文件保存路径+XXX。ZIP
    :return:
    '''
    zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)

    for path,dirnames,filenames in os.walk(dirpath,onerror='FileNotFoundError'):
        #去掉目标跟路径，只对目标文件夹下边的文件及文件夹压缩
        fpath = path.replace(dirpath,'')
        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
        zip.close()

if __name__ == '__main__':
    zipDir('../report/report/html','../../result/report/apiAutoTestReport.zip')
    print('压缩完成！')