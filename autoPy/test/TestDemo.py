import json
import re
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
    def fdict(self, **value_dict):
        #以字典做为参数只能用**传入
        a = ['a','b','c']
        str =  "<DATAROOT><DATAROW><BL_CODE>bl_code</BL_CODE><UA_CODE>ua_code</UA_CODE><RESULT_MSG>BATT_TYPE不正确</RESULT_MSG></DATAROW></DATAROOT>"
        pattern = re.compile('<' + "bl_code" + '>(.*)</' + "bl_code" + '>',re.I)
        result_list = pattern.findall(str)
        print(len(result_list))
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


if __name__ == "__main__":
    t = TestDemo()
    t.udict()
