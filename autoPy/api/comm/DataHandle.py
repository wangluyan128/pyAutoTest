import re
import json

#递归调用，更新json中的字段值
def update_json_step(node,json_str,value,i = 0):
    #当前节点索引（负向)
    node_index = -len(node) + i
    #如果包含[n]形式，说明节点为列表，需处理
    if '[' in node[node_index] and ']' in node[node_index]:
        list_node,list_index = node[node_index].split('[')
        index = list_index.split(']')[0]
        if index is None or index == '':
            print('参数传入错误，请指定列表[%]索引' %list_node)
        else:
            index = int(index)
        return update_json_step(node,json_str[list_node][index],value,i+1)
        #判断如果当前节点为最后一个节点，则更新value值
        if node_index == -1:
            json_str[node[-1]] = value
        return json_str
    return update_json_step(node,json_str[node[node_index]],value,i+1)

class DataHandle:
    def __init__(self,data_type,data_msg,fields,value_dict=None):
        '''
        处理请求体或响应体数据，读取或更新字段值
        :param data_type: 数据类型：xml,json
        :param data_msg: 请求体或响应体
        :param fields: 字段值，支持多字读方式，字估间逗号隔开；或传入列表、元组
                        json格式：需写入完整节点路径，如：body.base.name,
                        对应list类型的需传入索引位置，如：body.baselist[0].name
        :param value_dict:以字典键值对保存字段值
        '''
        self.data_type = data_type
        self.data = data_msg
        #fields支持str,list方式，str自动转换为list
        if isinstance(fields,str):
            self.feilds = fields
            self.feilds_list = []
            if ',' in fields:#strip()移除字符串头尾指定的字符
                self.feilds_list = fields.strip().split(',')
            else:
                self.feilds_list.append(fields.strip())
        elif isinstance(fields,list):
            self.feilds_list = fields
        else:
            self.feilds_list = list(fields)
        #初始化字典值
        if value_dict is None:
            self.value_dict = dict()
        else:
            self.value_dict = value_dict

    def get_fields_value(self):
        '''
        获取字段值
        1.支持获取多个字段值，输入字符串或列表，元组
        :return:
        '''
        step_dict = self.value_dict
        #字段列表循环获取
        for p in self.feilds_list:
            if p == '':
                continue
            #处理xml格式报文
            if self.data_type.upper()=='XML':
                pattern = '<' + p + '>.*</' + p + '>'
                search_result = re.search(pattern,self.data)
                if search_result is not None:
                    #包括标签和值都匹配上
                    field_and_value = search_result.group()
                    #去除标签获取字段值，并存入字典
                   # step_dict[p] = (field_and_value.split('</'))[0].split('>')[-1]
                    step_dict[p] = field_and_value.split('</')[0].split('>')[-1].split('<')[0]
                else:
                    print('参数[%s]提取失败，无匹配值。' %p)
            #处理json格式报文
            elif self.data_type.upper()=='JSON':
                #获取层级(使用.隔开)
                node = p.split('.')
                #json转换字典
                if isinstance(self.data,dict):
                    temp = self.data
                else:
                    temp = json.loads(self.data)
                #逐层读取数据
                for per_node in node:
                    if '[' in per_node and ']' in per_node:
                        per_node,index_str = per_node.split('[')
                        index = int(index_str.split(']')[0])
                        temp = temp.get(per_node)[index]
                        if temp is None:
                            break
                    else:
                        try:
                            temp = temp.get(per_node)
                            if temp is None:
                                break
                        except:
                            print("ERROR:获取节点失败")
                #将读取的结果写入字典
                step_dict[p] = temp
            #非xml，json的数据格式，报错退出
            else:
                print('ERROR:不支持此数据类型[%]'%self.data_type)
        return step_dict

    def update_fields_value(self):
        '''
        更新字段值
        支持更新单个字段值，多个字段值（字段名 字符串或列表、元组，字段值 字典
        :return:
        '''
        req_body = self.data
        #字段列表循环更新
        for p in self.feilds_list:
            #入参类型判断
            if isinstance(self.value_dict,dict):
                #参数在字典中不存在,则跳过
                if p not in self.value_dict.keys():
                    print('ERROR:字典中不存在参数[%]'%p)
                    continue
                #获取字典中参数的值
                value = self.value_dict[p]
            elif isinstance(self.value_dict,str):
                value = self.value_dict
            else:
                print('函数入参[%]类型不支持，请传入字符串或字典。'%self.value_dict)
                break
            #更新数据类型为xml的参数值
            if self.data_type.upper() == 'XML':
                #优先寻找是否存在指定更新参数，若有，则按指定参数更新
                if '${' + p + "}" in req_body:
                    req_body = req_body.replace('${' + p + '}',value)
                #其次寻找标签参数值，若有，则热裤标签更新值
                else:
                    #检查标签是否存在，若存在
                    if '<' + '>' in req_body and '</' + p + '>' in req_body:
                        #正则匹配
                        pattern = '<' + p + '>.*</' + p + '>'
                        new_field_and_value = '<' + p + '>' + str(value) + '</' + p + '>'
                        search_result = re.search(pattern,req_body)
                        #若正则匹配结果存在，则进行字段值更新
                        if search_result is not None:
                            old_field_and_value = search_result.group()
                            req_body = req_body.replace(old_field_and_value,new_field_and_value)
                        else:
                            print('参数[%s]匹配标签失败，无此标签。' %p)
                    else:
                        #print('参数[%s]匹配标签失败，无此标签。'%p)
                        continue
            #更新数据类型为xml的参数值
            elif self.data_type.upper() == 'JSON':
                #json转换字典
                if isinstance(self.data,dict):
                    req_body = self.data
                else:
                    req_body = json.loads(self.data)
                #获取层级
                node = p.split('.')
                #调用递归函数更新字段值
                update_json_step(node,req_body,value)
            #非xml,json的数据格式，报错退出
            else:
                print('ERROR:不支持此数据类型【%s】' %self.data_type)
                break
        return req_body

