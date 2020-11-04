from api.comm.data_handle import DataHandle

def intf_base_init(data_type,request_body,**kwargs):
    '''
    接口初始化通用类
    :param data_type:数据类型，如：xml,json
    :param request_body: 请求体
    :param kwargs: 可变关键字参数
    :return: 请求体
    '''
    return DataHandle(data_type,request_body,kwargs.keys(),kwargs).update_fields_value()