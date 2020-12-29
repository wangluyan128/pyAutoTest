#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
import json
import os
import re
import zipfile
from collections import OrderedDict
from urllib import request

import filetype
import jsonpath
import pytest
import requests

from api.utils.ReadData import ReadData
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor


class TestDemo:
    def __init__(self):
        d = dict(name = 'Bob',age = 20,score = 88)

    def a(self): #dict字典的几种定义方式
        c = dict(name = 'Bob',age = 20,score = 88)
        e = {"name":'Bob',"age":20,"score":88}
        f = dict([["name","zh"],["age","18"]])
        ff = dict([("name",'zh'),("age",18)])
        d = {"a":['a'],"b":['a.b[0]']}
        print(c)
        print(e)
        print(f)
        print(ff)
        print(d)
    def m(self):
        a = ["a", "b", "c"]
        b = [1,2,3]
        c = ["w"]
        d = zip(c,a)
        print(list(d))

    def n(self):
        a = "<a>bbb</a>"
        print((a.split('/'))[0].split('>')[-1].split('<')[0])
        print((a.split('/'))[0])

    def nn(self):
        a ='{  \
            "name":"网站", \
            "num":3, \
            "sites":[ \
                {"name":"Goolge","info":["Android","Goolge搜索","Goolge翻译"]}, \
                {"name":"Runoob","info":["菜鸟教程","菜鸟工具","菜鸟微信"]}, \
                {"name":"Taobao","info":["淘宝","网购"]} \
            ] \
            }'
        temp = json.loads(a);
        node = "sites[-2].info".split('.')
        print(jsonpath.jsonpath(temp,'$..sites[-1].name'))
        # print(temp["sites"][1]["info"])
        #逐层读取数据
        for per_node in node:
            if '[' in per_node and ']' in per_node:
                per_node,index_str = per_node.split('[')
                index = int(index_str.split(']')[0])
                temp = temp.get(per_node)[index]
                print("1 "+ per_node)
                print("1 " + str(index))
                if temp is None:
                    break
            else:
                try:
                    temp = temp.get(per_node)
                    if temp is None:
                        break
                    print(temp)
                except:
                    print("Error: 获取节点失败")
    #def fdict(self, **value_dict):
    def fdict(self, value_dict=None):
        #以字典做为参数只能用**传入
        a = ['a','b','c']
        str =  "<DATAROOT><DATAROW><BL_CODE>bl_code</BL_CODE><UA_CODE>ua_code</UA_CODE><RESULT_MSG>BATT_TYPE不正确</RESULT_MSG></DATAROW></DATAROOT>"
        pattern = re.compile('<' + "bl_code" + '>(.*)</' + "bl_code" + '>',re.I)
        result_list = pattern.findall(str)
        print(len(result_list))
        if value_dict is None:
            value_dict = dict()
            #value_dict = dict()
            value_dict['bl_code'] = result_list
            print(value_dict)


    def udict(self):
        body = "<DATAROOT><DATAROW><BL_CODE>bl_code</BL_CODE><UA_CODE>ua_code</UA_CODE><RESULT_MSG>BATT_TYPE不正确</RESULT_MSG></DATAROW></DATAROOT>"
        value = {"BL_CODE":"aa"}
        #正则匹配规则
        pattern = re.compile('<' + "BL_CODE" + '>.*</' + "BL_CODE" + '>',re.I)
        #1.值为字符串，更新参数值
        if isinstance(value,str):
            #只替换第一个
            new_value = '<' + "BL_CODE" + '>' + "ok" + '</' + "BL_CODE" + '>'
            body = re.sub(pattern,new_value,body,count = 1)
        # print(body)
        # return body
        #2.值为列表或元组等序列
        #匹配搜索所有满足项
        findall = pattern.findall(body)
        print(findall)
        print(len(value))
        if len(findall) != len(value):

            print('传入参数[%s],值长度与实际长度[%s]不匹配。' %(value,len(findall)))
            return None
        print(value)
        print(findall)
        for n,o in zip(value,findall):
            print("2" + o)
            print("n" + n)
            old_value = o
            new_value = '<' + 'BL_CODE' + '>' + n + '</' +'BL_CODE' + '>'
            print("3" + new_value)
            body = body.replace(old_value,new_value,1)
        print(body)

    def node1(self):
        body ={'a':['a'],'b':['a.b[0]'],'c':['a.b[0].c[0]','a.b[0].c[1]']}
        node = "a.b.c"
        #l = list(node.values())[0]
        # els = list(node.items())

        node_key=dict(zip(node,[[] for x in node]))
        node_key_data = dict(zip(node,[[] for x in node]))
        # print(node_key)
        for n in range(len(node)):
            if n == 0:
                #print(node[0])
                if node[0] not in body:
                    print("aaaa")
                node_key[node[0]].append(node[0])
                node_key_data[node[0]].append(body[node[0]])
            node_bak = node_key[node[n-1]]
            print(node_bak)
            back_data = node_key_data[node[n-1]]
        print(back_data)

    def l1(self):
        a = {'q':1,'w':[]}
        b = a.copy()
        b['q'] = 2
        b['w'].append(123)
        print(a)
        print(b)

        a1 = {'q':1,'w':[]}
        b1 = a1.copy()
        b1['q'] = 2
        b1['w'] = [123]
        print(a1)
        print(b1)

    def a1(self):
        # node = "body.baselist[0].name"
        node = "list.sites[1].info"
        node2 = node.split('.')
        #print(node2)
        data_dict ='{  \
            "name":"网站", \
            "num":3, \
            "list":{    \
                "sites":[ \
                    {"name":"Goolge","info":["Android","Goolge搜索","Goolge翻译"]}, \
                    {"name":"Runoob","info":["菜鸟教程","菜鸟工具","菜鸟微信"]}, \
                    {"name":"Taobao","info":["淘宝","网购"]} \
            ]} \
            }'
        node1 = "'b':['a.b[0]']"
        node_key_data = dict()
        node_key =dict(zip(node2,[[] for x in node2]))
        node_key_data = dict(zip(node2,[[] for x in node2]))
        try:
            for n in range(len(node2)):
                if n ==0:
                    if node2[0] not in data_dict:
                        break
                    node_key[node2[0]].append(node2[0])
                    node_key_data[node2[0]].append(json.loads(data_dict)[node2[0]])
                    print(node_key_data)
                    continue
                back_data = node_key_data[node2[n-1]]
                #print(node_key[n])
                back_no = len(node_key[node2[n-1]])
                print(back_no)
                for v in range(back_no):
                    print(back_data[v])
                    if node2[n] not in back_data[v]:
                        # print(node2[n])
                        if '[' in node2[n] and ']' in node2[n]:
                            node_key[node2[n]].append(node_key[node2[n-1]][v] + '.' + node2[n])
                            # print(node_key[node2[n]])
                            this_node,this_node_index_str = node2[n].split('[')
                            try:
                                this_node_index = int(this_node_index_str.split(']')[0])
                                print("adfs "+str(this_node_index))
                            except:
                                print('参数节点[%s]索引不存在。'%node2[n])
                                this_node_index = None
                            print("3333333")
                            node_key_data[node2[n]].append(back_data[v][this_node][this_node_index])
                            print("DDDD"+str(node_key_data[node2[n]]))
                            continue
                        else:
                            continue
                    #当前路径，当前节点的数据

                    # print("111111111111"+ str(back_data[v][node2[n]]))
                    print("22222222")
                    cur_node_data = back_data[v][node2[n]]
                    print("3333333"+str(cur_node_data))

                    #判断如果是字典，说明不用细分，直接获取对应的节点名称以及节点数据值即可
                    if isinstance(cur_node_data,dict):
                        node_key[node2[n]].append(node_key[node2[n-1]][v] + '.' + node2[n])
                        node_key_data[node2[n]].append(cur_node_data)
                        continue
                        if n == len(node) - 1:
                            node_key[node2[n]].append(node_key[node2[n - 1]][v] + '.' + node2[n])
                        node_key_data[node2[n]].append(cur_node_data)
                        continue

                    #前面的情况都不是，那么只剩下最后一种，该节点对应数据为列表形式了
                    #获取列表长度
                    cur_node_len = len(cur_node_data)
                    #第三重循环，根据列表数量，分别需要组合前面的节点路径，再获取对应的节点名以及节点数据
                    for vn in range(cur_node_len):
                        node_key[node2[n]].append(node_key[node2[n - 1]][v] + '.' + node2[n] + '[' + str(vn) + ']')
                        node_key_data[node2[n]].append(cur_node_data[vn])
                    #print(node_key)
                    #print(node_key_data)
        except:
            pass
            #判断如果节点没有嵌套列表这种，就不用多层返回了

        if node_key[node2[-1]]:
            value_dict = dict()
            #内层key和外层key相等
            if '.'.join(node2) == node_key[node2[-1]][0]:
                print(type(node_key_data[node2[-1]][0]))
                value_dict['.'.join(node2)] = node_key_data[node2[-1]][0]
            #嵌套2层字典的场景
            else:
                print(dict(zip(node_key[node2[-1]],node_key_data[node2[-1]])))
                value_dict['.'.join(node2)] = dict(zip(node_key[node2[-1]],node_key_data[node2[-1]]))
        else:
            value_dict['.'.join(node2)] = None
        print(value_dict)

    def a2(self):

        for i in range(1):
            if i == 0:
                try:
                    print("aa")
                except:
                    print("cc")
                print("dd")
                continue
            else:
                continue
            print("bb")

        l1 = ['a','b','c']
        file_path_list = eval("[\"/Users/zy7y/Desktop/vue.js\",\"/Users/zy7y/Desktop/jenkins.war\"]")
        print(file_path_list)

    def a3(self):
        i= 0;
        node = ["list","sites[1]","info"]
        json_str ='{  \
            "name":"网站", \
            "num":3, \
            "list":{    \
                "sites":[ \
                    {"name":"Goolge","info":["Android","Goolge搜索","Goolge翻译"]}, \
                    {"name":"Runoob","info":["菜鸟教程","菜鸟工具","菜鸟微信"]}, \
                    {"name":"Taobao","info":["淘宝","网购"]} \
            ]} \
            }'
        json1 = json.loads(json_str)
        print(json1.items())
        for dk,dv in json1.items():
            print(dk+" "+ dv)
        print(json.loads(json_str)[node[0]])
        node_index = -len(node) + i
        print(node_index)
        print(node[node_index])
        if node[node_index] not in json_str:
            #如果包含[n]形式，说明节点为列表，需处理
            if '[' in node[node_index] and ']' in node[node_index]:
                list_node,list_index = node[node_index].split('[')
                index = list_index.split(']')[0]
                if index is None or index == '':
                    print('ERROR:[%s]参数传入错误，请指定列表[%s]索引.' %(node,list_node))
                    return False
                else:
                    index = int(index)
            # return is_exist_node(node,json_str[list_node],i +1)
            else:
                print('[%s]字段节点[%s]不存在。' %(node,node[node_index]))
                return False
            #判断如果当前节点为最后一个节点，则返回True
        if node_index == -1:
            return True

    #return is_exist_node(node,json_str[node[node_index]],i + 1)
    def jsonpathdemo(self):
        json_str ={
            "store": {
                "book": [
                    { "category": "reference",
                        "author": "Nigel Rees",
                        "title": "Sayings of the Century",
                        "price": 8.95
                    },
                    { "category": "fiction",
                        "author": "Evelyn Waugh",
                        "title": "Sword of Honour",
                        "price": 12.99
                    },
                    {   "category": "fiction",
                        "author": "Herman Melville",
                        "title": "Moby Dick",
                        "isbn": "0-553-21311-3",
                        "price": 8.99
                    },
                    {   "category": "fiction",
                        "author": "J. R. R. Tolkien",
                        "title": "The Lord of the Rings",
                        "isbn": "0-395-19395-8",
                        "price": 22.99
                    }
                    ],
                    "bicycle": {
                    "color": "red",
                    "price": 19.95
                }
            }
        }
        str ='{"case_002": ["$.data.id"],"case_001":["$.meta.msg","$.meta.status"]}'

        print(jsonpath.jsonpath(json_str,'$.store.book[*].author'))
        print(jsonpath.jsonpath(json_str,'$.store.book[?(@.categrory=="reference")]'))
        print(jsonpath.jsonpath(json_str,'$..book[?(@.isbn)'))      #获取所有具有isbn属性的书
        print(jsonpath.jsonpath(json_str,'$..book[?(@.price<10)]'))  #获取price小于10 的书

        str1 = '{"dhId":"wangyan","key":"666"}'
        str2 = '{"name":"zhangsan","age":"17","email":"123@163.com"}'
        list1 = ['success', 0, 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMTI5IiwiZXhwIjoxNjA2OTM4NTUwfQ.QcWcCc_Ler2ghZMcR4vCp9HWkVaUBgBzTrlMB7jLPf_rEresZgVcWDBOdWrwC6i3QI5rl91G8e8INbs872atbg']
        mylist = [123, {'name': 'dragon'}, {'location': ('ch', 'nt')}]
        print(type(str1))
        data = json.loads(str1)
        print(data)
        json.dumps(mylist,ensure_ascii=False)
        dict1 = {'message': 'success', 'code': 0, 'data': {'content': [{'id': 147, 'name': '电梦网络测试组', 'orgId': 265, 'orgType': 1, 'pid': 0, 'status': 0, 'pms': 'fangwei', 'adminUsers': 'zhujun,shencenwei', 'products': '5', 'productList': [{'id': 5, 'uniqId': 1330466377, 'enName': 'Omni Adventure', 'name': '放置旅团', 'icon': 'https://open.17m3.com/uploadfiles/developer/2019/07/26/20190726162608.png', 'status': 1, 'createdAt': '1999-01-01 00:00:00', 'updatedAt': '2020-10-20 11:18:26'}], 'adminUserList': [{'id': 78, 'dhId': 'shencenwei', 'name': '沈岑伟', 'admin': 0, 'superAdmin': True, 'deptAdmin': False, 'companyId': 5, 'status': None, 'createdAt': '2020-10-20 10:28:27', 'updatedAt': '2020-12-02 00:00:25', 'department': {'id': 82, 'name': '运营开发部', 'orgId': 512, 'orgType': 3, 'pid': 509, 'status': 1, 'pms': 'anita,shencenwei', 'adminUsers': 'anita,fisn', 'products': '1,2,3', 'productList': None, 'adminUserList': None, 'pmsList': None, 'demandTypes': None, 'projects': None, 'createdAt': '2020-10-20 10:28:26', 'updatedAt': '2020-12-01 16:35:44'}}, {'id': 767, 'dhId': 'zhujun', 'name': '朱军', 'admin': 0, 'superAdmin': True, 'deptAdmin': True, 'companyId': 6, 'status': None, 'createdAt': '2020-10-20 14:39:29', 'updatedAt': '2020-10-20 14:39:29', 'department': {'id': 147, 'name': '电梦网络测试组', 'orgId': 265, 'orgType': 1, 'pid': 0, 'status': 0, 'pms': 'fangwei', 'adminUsers': 'zhujun,shencenwei', 'products': '5', 'productList': None, 'adminUserList': None, 'pmsList': None, 'demandTypes': None, 'projects': None, 'createdAt': '2020-10-20 14:39:26', 'updatedAt': '2020-11-21 00:00:06'}}], 'pmsList': [{'id': 787, 'dhId': 'fangwei', 'name': '方伟', 'admin': 0, 'superAdmin': False, 'deptAdmin': False, 'companyId': 6, 'status': None, 'createdAt': '2020-10-20 14:39:29', 'updatedAt': '2020-10-20 14:39:29', 'department': {'id': 147, 'name': '电梦网络测试组', 'orgId': 265, 'orgType': 1, 'pid': 0, 'status': 0, 'pms': 'fangwei', 'adminUsers': 'zhujun,shencenwei', 'products': '5', 'productList': None, 'adminUserList': None, 'pmsList': None, 'demandTypes': None, 'projects': None, 'createdAt': '2020-10-20 14:39:26', 'updatedAt': '2020-11-21 00:00:06'}}], 'demandTypes': [{'id': 37, 'name': '系统'}, {'id': 46, 'name': '设计'}, {'id': 44, 'name': '网站'}, {'id': 45, 'name': '测试'}], 'projects': [{'id': 20087261, 'name': '野蛮人大作战'}, {'id': 20108871, 'name': '游戏引入评测'}], 'createdAt': '2020-10-20 14:39:26', 'updatedAt': '2020-11-21 00:00:06'}], 'page': 0, 'size': 20, 'total': 1}}
        dict2 = [{'id': 5, 'uniqId': 1330466377, 'enName': 'Omni Adventure', 'name': '放置旅团', 'icon': 'https://open.17m3.com/uploadfiles/developer/2019/07/26/20190726162608.png', 'status': 1, 'createdAt': '1999-01-01 00:00:00', 'updatedAt': '2020-10-20 11:18:26'}]
        print(jsonpath.jsonpath(dict1,'$.[message,code]'))
        print(type(['success', 0]))

    def zipDemo(self):
        zip = zipfile.ZipFile('../result/report/apiAutoTestReport.zip',"w",zipfile.ZIP_DEFLATED)

        for path,dirnames,filenames in os.walk('../result/report/html',onerror='FileNotFoundError'):
        #去掉目标跟路径，只对目标文件夹下边的文件及文件夹压缩
            print('1111')
            fpath = path.replace('../result/report/html','')
            print(path)
            print(filenames)
            for filename in filenames:
                zip.write(path,filename)

#            for filename in filenames:
#                zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
            zip.close()

#        zfile = zipfile.ZipFile("test.zip","w")
#        zfile.write(r"./a/1.txt")
#        zfile.close()
    def pathDemo(self):
        str1 = "{\"message\": \"success\", \"code\": 0, \"data\": [{\"id\": 161, \"name\": \"\u7814\u53d1\u4e2d\u5fc3\", \"orgId\": 558, \"orgType\": 1, \"pid\": 0, \"status\": 1, \"pms\": \"zhouyuzhe\", \"adminUsers\": \"wangyan\", \"products\": \"1,2,3,4,5,6,7,50\", \"productList\": [{\"id\": 1, \"uniqId\": 1364020563, \"enName\": \"qmms\", \"name\": \"\u5168\u6c11\u68a6\u4e09\u56fd\", \"icon\": \"https://open.17m3.com/uploadfiles/developer/2019/07/19/20190719163319.jpg\", \"status\": 1, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 10:35:20\"}, {\"id\": 2, \"uniqId\": 1498630723, \"enName\": \"\uc694\uc2e0\uae30\", \"name\": \"\u5996\u795e\u8bb0\", \"icon\": \"https://open.17m3.com/uploadfiles/developer/1498630723/20191227192306.png\", \"status\": 1, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 11:18:24\"}, {\"id\": 3, \"uniqId\": 1397180240, \"enName\": \"\uc0bc\uad6d\uc81c\ud328\", \"name\": \"\u4e09\u56fd\u8ba1\uff08\u97e9\u56fd\uff09\", \"icon\": \"https://open.17m3.com/uploadfiles/developer/1397180240/20200207163305.png\", \"status\": 1, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 11:18:25\"}, {\"id\": 4, \"uniqId\": 1145461315, \"enName\": \"DC Ultimate Arena\", \"name\": \"DC\u5dc5\u5cf0\u6218\u573a\", \"icon\": \"https://api-hd.om.dianhun.cn/file/uploads/file/babd78154fb34c349dca0cfe905ea78c.png\", \"status\": 1, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 11:18:26\"}, {\"id\": 5, \"uniqId\": 1330466377, \"enName\": \"Omni Adventure\", \"name\": \"\u653e\u7f6e\u65c5\u56e2\", \"icon\": \"https://open.17m3.com/uploadfiles/developer/2019/07/26/20190726162608.png\", \"status\": 1, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 11:18:26\"}, {\"id\": 6, \"uniqId\": 1313425985, \"enName\": \"Ninja Storm\", \"name\": \"Ninja Storm\", \"icon\": \"https://open.17m3.com/uploadfiles/developer/1313425985/20191227164758.jpg\", \"status\": 0, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 10:28:32\"}, {\"id\": 7, \"uniqId\": 1498045018, \"enName\": \"\u7570\u754c\u6226\u4e89\", \"name\": \"\u7570\u754c\u6226\u8a18\", \"icon\": \"https://open.17m3.com/uploadfiles/developer/2019/09/26/20190926152445.png\", \"status\": 0, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 10:28:32\"}, {\"id\": 50, \"uniqId\": 1145590595, \"enName\": \"\", \"name\": \"\u68a6\u5e73\u53f0\u5546\u57ce\", \"icon\": \"https://open.17m3.com/uploadfiles/Temp/2015-11-11/20151111150315342.jpg\", \"status\": 0, \"createdAt\": \"1999-01-01 00:00:00\", \"updatedAt\": \"2020-10-20 10:28:33\"}], \"adminUserList\": [{\"id\": 1129, \"dhId\": \"wangyan\", \"name\": \"\u738b\u5ca9\", \"admin\": 1, \"superAdmin\": false, \"deptAdmin\": false, \"companyId\": 6, \"status\": null, \"createdAt\": \"2020-10-23 18:24:24\", \"updatedAt\": \"2020-10-29 09:49:34\", \"department\": {\"id\": 147, \"name\": \"\u7535\u68a6\u7f51\u7edc\u6d4b\u8bd5\u7ec4\", \"orgId\": 265, \"orgType\": 1, \"pid\": 0, \"status\": 0, \"pms\": \"fangwei\", \"adminUsers\": \"zhujun,shencenwei\", \"products\": \"5\", \"productList\": null, \"adminUserList\": null, \"pmsList\": null, \"demandTypes\": null, \"projects\": null, \"createdAt\": \"2020-10-20 14:39:26\", \"updatedAt\": \"2020-11-21 00:00:06\"}}], \"pmsList\": [{\"id\": 1123, \"dhId\": \"zhouyuzhe\", \"name\": \"\u5468\u8c6b\u54f2\", \"admin\": 0, \"superAdmin\": false, \"deptAdmin\": false, \"companyId\": 6, \"status\": null, \"createdAt\": \"2020-10-20 14:39:31\", \"updatedAt\": \"2020-10-20 14:39:31\", \"department\": {\"id\": 147, \"name\": \"\u7535\u68a6\u7f51\u7edc\u6d4b\u8bd5\u7ec4\", \"orgId\": 265, \"orgType\": 1, \"pid\": 0, \"status\": 0, \"pms\": \"fangwei\", \"adminUsers\": \"zhujun,shencenwei\", \"products\": \"5\", \"productList\": null, \"adminUserList\": null, \"pmsList\": null, \"demandTypes\": null, \"projects\": null, \"createdAt\": \"2020-10-20 14:39:26\", \"updatedAt\": \"2020-11-21 00:00:06\"}}], \"demandTypes\": [{\"id\": 51, \"name\": \"\u7f51\u7ad9\"}, {\"id\": 52, \"name\": \"\u6d4b\u8bd5\"}, {\"id\": 53, \"name\": \"\u8bbe\u8ba1\"}, {\"id\": 50, \"name\": \"\u7cfb\u7edf\"}], \"projects\": [], \"createdAt\": \"2020-10-20 14:39:27\", \"updatedAt\": \"2020-11-03 10:16:25\"}]}"
        jsonstr = json.loads(str1)
        list1 = ['', [147]]
        for i in range(len(list1)):
            if isinstance(list1[i],list):
                #list[l] = l[0]
                print(list1[i])
                list1[i] = list1[i][0]
        print(list1)

        list2 = list(map(str,list1))
        print(list2)
        parameters_path_url = "/".join(list2)
        print(parameters_path_url)

        print(jsonpath.jsonpath(jsonstr,"$.data[0].adminUserList[0].department.id"))

    def jsonpathDemo1(self):
        '''
        操作	说明
        $	查询根元素。这将启动所有路径表达式。
        @	当前节点由过滤谓词处理。
        *	通配符，必要时可用任何地方的名称或数字。
        ..	深层扫描。 必要时在任何地方可以使用名称。
        .<name> 点，表示子节点
        ['<name>' (, '<name>')] 括号表示子项
        [<number> (, <number>)] 数组索引或索引
        [start:end]             数组切片操作
        [?(<expression>)]	    过滤表达式。 表达式必须求值为一个布尔值。
        =====================
        XPath   JSONPath    描述
        /       $           根节点
        .       @           现行节点
        /       .or[]       取子节点
        ..      n/a         取父节点，Jsonpath未支持
        //      ..          就是不管位置，选择所有符合条件的条件
        *       *           匹配所有元素节点
        @       n/a         根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要属性访问。
        []      []          迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等）
        |       [,]         支持迭代器中做多选。
        []      ?()         支持过滤操作.
        n/a     ()          支持表达式计算
        ()      n/a         分组，JsonPath不支持
        =====================
        函数	描述	输出
        min()	提供数字数组的最小值	Double
        max()	提供数字数组的最大值	Double
        avg()	提供数字数组的平均值	Double
        stddev()	提供数字数组的标准偏差值	Double
        length()	提供数组的长度	Integer
        =====================
        操作符	描述
        ==	left等于right（注意1不等于'1'）
        !=	不等于
        <	小于
        <=	小于等于
        >	大于
        >=	大于等于
        =~	匹配正则表达式[?(@.name =~ /foo.*?/i)]
        in	左边存在于右边 [?(@.size in ['S', 'M'])]
        nin	左边不存在于右边
        size	（数组或字符串）长度
        empty	（数组或字符串）为空
        '''
        json_str ={
            "store": {
                "book": [
                    {
                        "category": "reference",
                        "author": "Nigel Rees",
                        "title": "Sayings of the Century",
                        "price": 8.95
                    },
                    {
                        "category": "fiction",
                        "author": "Evelyn Waugh",
                        "title": "Sword of Honour",
                        "price": 12.99
                    },
                    {
                        "category": "fiction",
                        "author": "Herman Melville",
                        "title": "Moby Dick",
                        "isbn": "0-553-21311-3",
                        "price": 8.99
                    },
                    {
                        "category": "fiction",
                        "author": "J. R. R. Tolkien",
                        "title": "The Lord of the Rings",
                        "isbn": "0-395-19395-8",
                        "price": 22.99
                    }
                ],
                "bicycle": {
                        "color": "red",
                        "price": 19.95
                    }
                },
                "expensive": 10
            }
        #jsondemo = json.dumps(json_str)
        print("获取json中store下book下的所有author值")
        print(jsonpath.jsonpath(json_str,"$.store.book[*].author"))
        print("获取所有json中所有author的值")
        print(jsonpath.jsonpath(json_str,"$..author"))
        print("所有的东西，书籍和自行车")
        print(jsonpath.jsonpath(json_str,"$.store.*"))
        print("获取json中store下所有price的值")
        print(jsonpath.jsonpath(json_str,"$.store..price"))
        print("获取json中book数组的第3个值")
        print(jsonpath.jsonpath(json_str,"$..book[2]"))
        print("倒数的第二本书")
        print(jsonpath.jsonpath(json_str,"$..book[-2]"))
        print("前两本书")
        print(jsonpath.jsonpath(json_str,"$..book[0,1]"))
        print("	从索引0（包括）到索引2（排除）的所有图书")
        print(jsonpath.jsonpath(json_str,"$..book[:2]"))
        print("从索引1（包括）到索引2（排除）的所有图书")
        print(jsonpath.jsonpath(json_str,"$..book[1:2]"))
        print("获取json中book数组的最后两个值")
        print(jsonpath.jsonpath(json_str,"$..book[-2:]"))
        print("	获取json中book数组的第3个到最后一个的区间值")
        print(jsonpath.jsonpath(json_str,"$..book[2:]"))
        print("获取json中book数组中包含isbn的所有值")
        print(jsonpath.jsonpath(json_str,"$..book[?(@.isbn)]"))
        print("获取json中book数组中price<10的所有值")
        print(jsonpath.jsonpath(json_str,"$.store.book[?(@.price < 10)]"))
        print("获取json中book数组中price<=expensive的所有值")
        print(jsonpath.jsonpath(json_str,"$..book[?(@.price <= $['expensive'])]"))
        print("获取json中book数组中的作者以REES结尾的所有值（REES不区分大小写）")
        print(jsonpath.jsonpath(json_str,"$..book[?(@.author =~ /.*REES/i)]"))
        print("逐层列出json中的所有值，层级由外到内")
        print(jsonpath.jsonpath(json_str,"$..*"))
        print("获取json中book数组的长度")
        print(jsonpath.jsonpath(json_str,"$..book.length()"))
        print("取到最后一个book的title")
        print(jsonpath.jsonpath(json_str,"$.store.book[(@.length-1)].title"))
        print("取到价格小于10的书的title")
        print(jsonpath.jsonpath(json_str,"$.store.book[?(@.price < 10)].title"))
        print("按步长取，到第1个和第3本书的titile")
        print(jsonpath.jsonpath(json_str,"$.store.book[0:3:2].title"))
        print("按步长取到第1本书的titile")
        print(jsonpath.jsonpath(json_str,"$.store.book[0:2:2].title"))
        print(jsonpath.jsonpath(json_str,"$.store.book[?(@.category=='reference')].title"))
        print(jsonpath.jsonpath(json_str,"$.store.book[(@.length-1)].price"))
    def test(self):
        str = "{\"case_011\":[\"$.data[?(@.name=='测试账号')].id\"]}"
        str1 = "{'case_011':['$.data[?(@.name=='测试账号‘)].id']}"
        print(json.loads(str))
        parameters = "/id"
        str2 = "{\"message\":\"success\",\"code\":0,\"data\":[{\"id\":6,\"dhId\":\"moore\",\"name\":\"张锐\",\"admin\":0,\"superAdmin\":null,\"deptAdmin\":null,\"companyId\":5,\"status\":1,\"createdAt\":\"2020-10-20 10:28:27\",\"updatedAt\":\"2020-12-22 00:00:23\",\"department\":{\"id\":60,\"name\":\"梦手游复刻版项目部\",\"orgId\":420,\"orgType\":3,\"pid\":42,\"status\":0,\"pms\":\"0\",\"adminUsers\":\"\",\"products\":null,\"productList\":null,\"adminUserList\":null,\"pmsList\":null,\"demandTypes\":[],\"projects\":[],\"createdAt\":\"2020-10-20 10:28:26\",\"updatedAt\":\"2020-10-20 10:28:26\"}},{\"id\":7,\"dhId\":\"liuyanqing\",\"name\":\"柳彦青\",\"admin\":0,\"superAdmin\":null,\"deptAdmin\":null,\"companyId\":5,\"status\":1,\"createdAt\":\"2020-10-20 10:28:27\",\"updatedAt\":\"2020-12-22 00:00:22\",\"department\":{\"id\":103,\"name\":\"X3项目部\",\"orgId\":535,\"orgType\":3,\"pid\":524,\"status\":0,\"pms\":\"0\",\"adminUsers\":\"\",\"products\":null,\"productList\":null,\"adminUserList\":null,\"pmsList\":null,\"demandTypes\":[],\"projects\":[],\"createdAt\":\"2020-10-20 10:28:26\",\"updatedAt\":\"2020-10-20 10:28:26\"}},{\"id\":8,\"dhId\":\"summersong\",\"name\":\"宋杰\",\"admin\":0,\"superAdmin\":null,\"deptAdmin\":null,\"companyId\":5,\"status\":1,\"createdAt\":\"2020-10-20 10:28:27\",\"updatedAt\":\"2020-11-20 00:00:09\",\"department\":{\"id\":91,\"name\":\"海外研发部\",\"orgId\":522,\"orgType\":3,\"pid\":11,\"status\":0,\"pms\":\"0\",\"adminUsers\":\"\",\"products\":null,\"productList\":null,\"adminUserList\":null,\"pmsList\":null,\"demandTypes\":[],\"projects\":[],\"createdAt\":\"2020-10-20 10:28:26\",\"updatedAt\":\"2020-11-21 00:00:06\"}}]}"
        str2 = json.loads(str2)
        str3 = "{\"message\":\"success\",\"code\":0,\"data\":{\"id\":13,\"dhId\":\"test30\",\"name\":\"测试账号\",\"admin\":0,\"superAdmin\":null,\"deptAdmin\":null,\"companyId\":6,\"status\":1,\"createdAt\":\"2020-10-23 18:24:24\",\"updatedAt\":\"2020-10-29 09:49:34\",\"department\":{\"id\":147,\"name\":\"电梦网络测试组\",\"orgId\":265,\"orgType\":1,\"pid\":0,\"status\":1,\"pms\":\"fangwei\",\"adminUsers\":\"zhujun,shencenwei\",\"products\":\"5\",\"productList\":null,\"adminUserList\":null,\"pmsList\":null,\"demandTypes\":[{\"id\":46,\"name\":\"设计\"},{\"id\":44,\"name\":\"网站\"},{\"id\":45,\"name\":\"测试\"},{\"id\":37,\"name\":\"系统\"}],\"projects\":[{\"id\":42,\"name\":null},{\"id\":41,\"name\":null}],\"createdAt\":\"2020-10-20 14:39:26\",\"updatedAt\":\"2020-12-21 14:33:44\"}}}"
        str3 = json.loads(str3)
        print(type(str3))
        print(jsonpath.jsonpath(str2,"$.data[?(@.name=='张锐')].dhId"))
        print(jsonpath.jsonpath(str3,"$.data.name"))
        print(parameters.replace("id","1275"))
    def up(self,filepath="E:\\1.jpg"):
        #根据文件路径，自动获取文件名称和文件minme类型
        a = filetype.guess(filepath)
        if a is None:
            print('cannot guess file_type!')
        #媒体类型
        typee = a.mime
        #文件真实路径
        realp = os.path.realpath(filepath)
        #获取文件名
        fname = os.path.split(filepath)[-1]
        return (fname,open(realp,'rb'),typee)
        #m = MultipartEncoder(
        #    filters=[
        #        ('source',up()),
        #    ]
        #)
    #r = request.post('http://httpbin.org/post',data=m,headers={'Content-Type':m.content_type})
    #print(r.text)

    def uploadDemo(self,file_path):
       #单文件上传
        files1 = {"file":open("1.jpg","rb")}
        #r1 =  requests.post("http://localhost:8888/upload",files = files1)

        #显式地设置文件名，文件类型和请求头：
        files2 = {'file':('1.jpg',open('1.jpg','rb'),'image/jpep',{'Expires':'0'})}
        #r2 = requests.post('http://localhost:8888/upload',files=files2)
        #多文件上传
        files3 = [
            ('files',('1.jpg',open('1.jpg','rb'),'image/jpeg')),
            ('files',('2.jpg',open('2.jpg','rb'),'image/jpeg'))

        ]
        if file_path.startswith('[') and file_path.endswith(']'):
           file_path_list = eval(file_path)    #字符串转成列表
           files3_1 = []
           for file_path in file_path_list:
               fileg = filetype.guess(file_path)
               if fileg is None:
                   print('cannot guess file_path!')
                #媒体类型
               typee = fileg.mime
               #获取文件名
               fname = os.path.split(file_path)[-1]
               files3_1.append(('files',(fname,open(file_path,'rb'),typee)))

        print(type(files3))
        r3 = requests.post('http://localhost:8888/uploads', files=files3_1)
        #上传时附带其他参数
        data = {
            "name":"upload",
            "age":100
        }
        files4 = [
            ('file',('1.jpg',open('1.jpg','rb'),'image/jpeg')),
            ('file',('2.jpg',open('2.jpg','rb'),'image/jpeg'))
        ]
        #r4 = requests.post('http://localhost:8888/upload',files=files4,data=data)
        #流式上传文件
        m = MultipartEncoder(
            fields={
                'name':'upload','age':'100',
                'file':('1.jpg',open('1.jpg','rb'),'image/jpeg'),
                'file':('2.jpg',open('2.jpg','rb'),'image/jpeg')
            }
        )
        #r5=requests.post('http://localhost:8888/upload',data=m,headers = {'Content-Type':m.content_type})
        #监听上传进度

        print(r3.content)
    def my_callback(self,monitor):
        progress = (monitor.bytes_read / len(monitor)) * 100
        print("\r文件上传进度：%d%%(%d/%d)" % (progress,monitor.bytes_read,len(monitor)), end=" ")

    e = MultipartEncoder(
        fields={
            'name':'unload','age':'100',
            'file':('1.jpg',open('1.jpg','rb'),'image/jpeg'),
            'file':('2.jpg',open('2.jpg','rb'),'image/jpeg')
        }
    )

#    m = MultipartEncoderMonitor(e,my_callback)
#    r6 = request.post('http://localhost:8888/upload',data=m,
#                      headers={'Content-Type':m.content_type})

if __name__ == "__main__":
    l1 = "['1.jpg','2.jpg']"
    t = TestDemo().uploadDemo(l1)


