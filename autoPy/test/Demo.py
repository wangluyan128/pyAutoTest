#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
import json
import re
from collections import OrderedDict

import jsonpath


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
        # print(temp)
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

if __name__ == "__main__":
    t = TestDemo()
    t.jsonpathdemo()